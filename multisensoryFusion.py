import math
import numpy as np
import pandas as pd
import tensorflow as tf
from scipy import signal
from scipy.io import loadmat
from keras.layers import Conv2D, Input, Dense, Flatten, AveragePooling2D
from keras.layers import concatenate, BatchNormalization, Activation, add
from keras.models import Model
from tensorflow.keras.regularizers import l2
from params import *

# Short time Fourier Transform
def stft_samples(index, filelist):
    label = np.empty(shape=(0),dtype=np.uint8)
    Comb = []
    for k in range(len(index)):
        Samples = np.empty(shape = (sample_size*len(filelist), crop_h, crop_w), dtype = np.float64)
        for i in range(len(filelist)):
            df = loadmat(DIR + filelist[i])[filelist[i][:-4]]['Y'][0][0][0][index[k]]['Data']
            data_list = map(lambda x: x[0], df.T)
            df = pd.Series(data_list)

            for j in range(sample_size):
                f, t, Zxx = signal.stft(df[j*sample_length:(j+1)*sample_length],
                                        fs = 128, nperseg = 128, noverlap = 120, nfft = 128)
                Zxx = tf.abs(Zxx)
                Zxx = Zxx[:crop_h,:crop_w]
                Samples[i*sample_size+j] = Zxx
            
            if k == 0:
                label = np.concatenate((label, np.ones(sample_size, dtype = np.uint8) * i))
                
        Samples = Samples.reshape((Samples.shape[0], crop_h, crop_w, 1))
        Comb.insert(k, Samples)

    Comb.append(label)
    return Comb

# Each seperate layer consists of convolution + BN + Relu in a Deep Residual Network
def residual_layer(inputs, num_filters, kernel = 3,
                   strides = 1, batch_norm = True, activation = True):

    x = inputs
    fx = Conv2D(num_filters, kernel_size = kernel, strides = strides, padding = 'same',
                kernel_initializer = 'he_normal', kernel_regularizer = l2(1e-4))(x)
    if batch_norm:
        fx = BatchNormalization()(fx)
    if activation:
        fx = Activation('relu')(fx)
    return fx

# Deep Residual Networks (17 layers for each type of signal, 1 for classification)
def resnet18(input_shape, num_classes, num_signals):
    num_residual_block_set = 4
    num_filters = 16
    num_residual_blocks = 2
    out_all = []
    x = []
    fx = []
    inputs = []
    
    # First Layer
    for k in range(num_signals):
        inputs.insert(k, Input(shape = input_shape))
        x.insert(k, residual_layer(inputs = inputs[k], num_filters = num_filters))
    
    # 4 x 2 Residual Blocks consist of 2 layers
    for res_block_set in range(num_residual_block_set):
        for res_block in range(num_residual_blocks):
            strides = 1
            if res_block_set > 0 and res_block == 0:  
                strides = 2
            for k in range(num_signals):
                fx.insert(k, residual_layer(inputs = x[k],
                                            num_filters = num_filters,
                                            strides=strides))
                fx[k] = residual_layer(inputs = fx[k],
                                       num_filters = num_filters,
                                       activation = False)
            # Downsizing input if required
            if res_block_set > 0 and res_block == 0:  
                for k in range(num_signals):
                    x[k] = residual_layer(inputs = x[k], num_filters = num_filters,
                                          kernel = 1, strides = strides,
                                          batch_norm = False, activation = False)
            for k in range(num_signals):
                # Element-wise addition
                x[k] = add([x[k], fx[k]])
                x[k] = Activation('relu')(x[k])
        num_filters *= 2
    
    for k in range(num_signals):
        x[k] = AveragePooling2D(pool_size=8)(x[k])
        out = Flatten()(x[k])
        out_all.insert(k, out)
    
    if num_signals == 1:
        out_final = out
    else:
        out_final = concatenate(out_all, name = "concat_signals")
    # Classification
    outputs = Dense(num_classes, activation = 'softmax', kernel_initializer = 'he_normal')(out_final)

    model = Model(inputs, outputs)
    return model

# Step Based Learning Rate Scheduling: lr is 0.001 for first (0.4*epochs) epochs and then multiplied by 0.1 at each (0.2*epochs) steps
def step_based_lr_schedule(epoch):
    lr = 1e-2
    d = 1e-1
    step = 40
    
    if epoch < step:
        lr = lr * d
    else:
        lr = lr * d**math.floor((1+epoch)/step)
    print('Learning rate: ', lr)
    return lr
