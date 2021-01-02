import os

# Selection of Dataset A, B, C or D
dataset = "A"

# PU Bearing Dataset Signal Index: [1] Current, [6] Vibration, [1, 6] Both
data_index = [6]

# Parameters for Input
size_h = 65
size_w = 65
crop_h = 64
crop_w = 64
sample_size = 400
sample_length = 512

# Parameters for Model Training
batch_size = 32
epochs = 2

# Parameters for STFT
fs = 128
nperseg = 128
noverlap = 120
nfft = 128

# Path for Data Files
DIR = (os.path.dirname(__file__) + './Dataset/')