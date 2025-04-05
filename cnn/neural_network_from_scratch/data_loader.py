#!/usr/bin/env python3

import os
import numpy as np
import struct
import git
import matplotlib.pyplot as plt
from array import array
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def get_git_root():
    return git.Repo(".", search_parent_directories=True).working_dir

# Define the paths of the files
WORK_DIR = get_git_root()
DATA_DIR = os.path.join(WORK_DIR, 'cnn/neural_network_from_scratch/data')
TRAIN_IMAGES_FILE_PATH = os.path.join(DATA_DIR, 'train-images.idx3-ubyte')
TRAIN_LABELS_FILE_PATH = os.path.join(DATA_DIR, ' ')
TEST_IMAGES_FILE_PATH = os.path.join(DATA_DIR, 'test-images.idx3-ubyte')
TEST_LABELS_FILE_PATH = os.path.join(DATA_DIR, 'test-labels.idx1-ubyte')

def read_idx3_ubyte(file_path):
    """
    Reads an IDX3-UBYTE file and returns the images as a NumPy array.
    :param file_path: Path to the IDX3-UBYTE file.
    :return: A NumPy array of shape (num_images, rows, cols).
    """
    with open(file_path, 'rb') as f:
        # Read the magic number, number of images, rows, and columns
        magic, num_images, rows, cols = struct.unpack(">IIII", f.read(16))
        
        # Ensure the magic number is correct (2051 for images)
        if magic != 2051:
            raise ValueError(f"Invalid magic number {magic} in file: {file_path}")
        
        # Read the image data
        images = np.frombuffer(f.read(), dtype=np.uint8)
        
        # Reshape into (num_images, rows, cols)
        images = images.reshape(num_images, rows, cols)
        
        return images

def show_images(image, timming=3000):
    def close_event():
        plt.close() #timer calls this function after 3 seconds and closes the window 

    fig = plt.figure()
    timer = fig.canvas.new_timer(interval = timming) #creating a timer object and setting an interval of 3000 milliseconds
    timer.add_callback(close_event)
    plt.imshow(image, cmap='gray')
    timer.start()
    plt.show()

def main():
    # Example usage
    images = read_idx3_ubyte(TEST_IMAGES_FILE_PATH)

    # Print the shape of the images array
    print(f"Loaded {images.shape[0]} images of size {images.shape[1]}x{images.shape[2]}")

    show_images(images[0]) # Display the first image
    
class MnistDataloader(object):
    """
    A class to load the MNIST dataset and split it into training, validation, and testing sets.
    """
    def __init__(self):
        self.load_data()
        
    def load_data(self):
        """
        Load the MNIST dataset and split it into training and testing sets.
        :return: Tuple of (X_train, y_train, X_test, y_test).
        """
        # scaler, X_train, y_train, X_val, y_val, X_test, y_test
        # Load the training data
        self.X_train = read_idx3_ubyte(TRAIN_IMAGES_FILE_PATH)
        self.y_train = read_idx3_ubyte(TRAIN_LABELS_FILE_PATH)

        # Load the testing data
        self.X_test = read_idx3_ubyte(TEST_IMAGES_FILE_PATH)
        self.y_test = read_idx3_ubyte(TEST_LABELS_FILE_PATH)

        
        
        # Split into train and validation set
        
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(self.X_train, self.y_train, test_size=0.05, stratify=self.y_train)
        
        # Standardize the train, validation and test dataset
        self.scaler = StandardScaler()
        self.scaler.fit(self.X_train)
        self.X_train = self.scaler.transform(self.X_train)
        self.X_val = self.scaler.transform(self.X_val)
        self.X_test = self.scaler.transform(self.X_test)
    
    def get_Xtrain(self):
        return self.X_train

    def get_ytrain(self):
        return self.y_train

    def get_Xval(self):
        return self.X_val

    def get_yval(self):
        return self.y_val

    def get_Xtest(self):
        return self.X_test

    def get_ytest(self):
        return self.y_test

    def get_scaler(self):
        return self.scaler
    
    def show_images(self, image, timming=3000):
        """
        Show the image using matplotlib.
        :param image: The image to show.
        :param timming: The time in milliseconds to show the image.
        """
        show_images(image, timming)