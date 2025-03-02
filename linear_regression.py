import numpy as np
import matplotlib.pyplot as plt
import git

def estimation_coef(x: np.array, y: np.array):
    # calculating number of observations
    # determines the number of data points
    n = np.size(x)

    # calculating means
    # compute the mean values of x and y, respectively
    x_mean = np.mean(x)
    y_mean = np.mean(y)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import os
from matplotlib.animation import FuncAnimation

def get_git_root():
    return git.Repo(".", search_parent_directories=True).working_dir

class Linear_regression():
    path_data_sets = os.path.join(get_git_root(), "data_set/data_for_lr.csv")
    data_sets = ""

    def __init__(self):
        print(self.path_data_sets)
        pass

    def coefficien(self):
        pass

    def read_data_csv(self):
        data = pd.read_csv()

if __name__ == "__main__":
    linear_regression = Linear_regression()
    # linear_regression.read_data_csv()
    # linear_regression.coefficien()