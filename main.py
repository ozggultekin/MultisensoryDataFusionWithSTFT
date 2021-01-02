import time
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow.keras.callbacks import ReduceLROnPlateau
from load_data import *
from multisensoryFusion import *
from utils import *
    
def main():
    X_train = []
    X_test = []
    X_val = []
    
    # Getting Dataset
    filelist, filelabel = dataset_selector(dataset)
      
    # Transforming Measured Signals to Spectrograms
    Comb = stft_samples(data_index, filelist)
    
    # Randomly Splitting Data Samples into Train, Validation and Test Sets
    splitter = np.arange(0, sample_size * len(filelist))
    train, test = train_test_split(splitter, test_size = 0.2, random_state = 42)
    train, val = train_test_split(train, test_size = 0.25, random_state = 42)
    
    for k in range(len(data_index)):
        X_train.insert(k, Comb[k][train])
        X_val.insert(k, Comb[k][val])
        X_test.insert(k, Comb[k][test])
    
    y_train = Comb[-1][train]
    y_val = Comb[-1][val]
    y_test = Comb[-1][test]
    
    # Creating Model by Regarding Number of Measured Signals
    model = resnet18(input_shape = X_train[0].shape[1:], num_classes = len(filelist), num_signals = len(index))
    
    # Optimizing with Adam optimizer based of Step Based Learning Rate Scheduling
    model.compile(loss='sparse_categorical_crossentropy', optimizer = Adam(lr = step_based_lr_schedule(0)), metrics = ['accuracy'])
    
    # Summary of Model
    model.summary()
    
    # Setting Callbacks
    start_time = time.time()
    lr_scheduler = LearningRateScheduler(step_based_lr_schedule)
    lr_reducer = ReduceLROnPlateau(factor = np.sqrt(0.1), cooldown = 0, patience = 5, min_lr = 0.5e-6)
    
    # Training Proposed Method with Train and Validation Sets
    history = model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs, validation_data = (X_val, y_val),
                        shuffle = True, callbacks = [lr_reducer, lr_scheduler], verbose = 2)
    
    # Testing with Test Set
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose = 2)
    y_pred = np.argmax(model.predict(X_test), axis = 1)
    print("\nTesting Accuracy:", test_acc)
    
    # Plotting Accuracy-Epoch Graph and Confusion Matrix
    plot_train_val_acc(history)
    plot_cnf_mtx(y_test, y_pred, filelabel)

if __name__ == '__main__':
    main()