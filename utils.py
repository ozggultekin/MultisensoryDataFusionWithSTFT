import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt

# Plot for Train and Validation Accuracy
def plot_train_val_acc(history):
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0, 1.025])
    plt.legend(loc='lower right')
    plt.show()

# Plotting Confusion Matrix
def plot_cnf_mtx(y_test, y_pred, filelabel):
    confusion_mtx = tf.math.confusion_matrix(y_test, y_pred) 
    plt.figure(figsize=(10, 8))
    sns.heatmap(confusion_mtx, xticklabels = filelabel, yticklabels = filelabel, annot=True, fmt = 'g')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()