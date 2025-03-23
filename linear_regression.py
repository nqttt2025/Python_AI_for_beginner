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


import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import os
import logging
from matplotlib.animation import FuncAnimation

class CustomFormatter(logging.Formatter):
    # Colors
    BLACK = "\033[0;30m"
    YELLOW = "\033[1;33m"
    GREEN = "\033[0;32m"
    RED = "\033[31;20m"
    BOLD_RED = "\033[31;1m"
    CYAN = "\033[0;36m"
    RESET = "\033[0m"

    # Formats
    ONLY_LEVEL_FMT = "%(asctime)s-[%(filename)s:%(lineno)d]-{}[%(levelname)s]{} - %(message)s"
    FULL_MSG_FMT = "{}%(asctime)s-[%(filename)s:%(lineno)d]-[%(levelname)s] - %(message)s{}"

    FORMATS = {
        logging.DEBUG: ONLY_LEVEL_FMT.format(CYAN, RESET),
        logging.INFO: ONLY_LEVEL_FMT.format(GREEN, RESET),
        logging.WARNING: FULL_MSG_FMT.format(YELLOW, RESET),
        logging.ERROR: FULL_MSG_FMT.format(RED, RESET),
        logging.CRITICAL: FULL_MSG_FMT.format(BOLD_RED, RESET)
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_git_root():
    return git.Repo(".", search_parent_directories=True).working_dir

def create_log_instance():
    if os.path.exists('{}/log_controler'.format(get_git_root())) is False:
        os.makedirs('{}/log_controler'.format(get_git_root()))
    if os.path.exists('{}/log_controler/app.log'.format(get_git_root())) is True:
        os.remove('{}/log_controler/app.log'.format(get_git_root()))

    # logger = logging
    # logger.basicConfig(filename='{}/log_controler/app.log'.format(get_git_root()),
    #                    level=logging.INFO,
    #                    filemode='w',
    #                    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create formatter
    __formatter = logging.Formatter('%(asctime)s-[%(filename)s:%(lineno)d]-[%(levelname)s] - %(message)s')
    __formatter.datefmt = "%H:%M:%S"

    # create console handler
    __ch = logging.StreamHandler(sys.stdout)
    __ch.setLevel(logging.DEBUG)
    __ch.setFormatter(CustomFormatter())

    # Create file handler
    fh = logging.FileHandler('{}/log_controler/app.log'.format(get_git_root()))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(__formatter)
    logger.addHandler(fh)
    logger.addHandler(__ch)
    return logger

class Linear_regression():
    path_data_sets = os.path.join(get_git_root(), "data_set/data_for_lr.csv")
    data_sets = ""
    logger = create_log_instance()
    parameters = {}

    def __init__(self):
        self.read_data_csv()

    def read_data_csv(self):
        data = pd.read_csv(self.path_data_sets)
        # drop the missing values
        self.data_sets = data.dropna()

    def reshape_data(self):
        # training data set and lable
        self.train_input = np.array(self.data_sets.x[0:500]).reshape(500, 1)
        self.train_output = np.array(self.data_sets.y[0:500]).reshape(500, 1)
        # valid data set and lable
        test_input = np.array(self.data_sets.x[500:700]).reshape(199, 1)
        test_output = np.array(self.data_sets.y[500:700]).reshape(199, 1)

    def forward_propagation(self, training_input):
        m = self.parameters['m']
        c = self.parameters['c']
        prediction = np.multiply(m, training_input) + c
        return prediction

    def cost_function(self, prediction, training_output):
        cost = np.mean((prediction - training_output) ** 2)
        return cost

    def backward_propagation(self, train_input, train_output, predictions):
        derivatives = {} #công cụ phái sinh
        df = (predictions-train_output)
        # dm= 2/n * mean of (predictions-actual) * input
        dm = 2 * np.mean(np.multiply(train_input, df))
        # dc = 2/n * mean of (predictions-actual)
        dc = 2 * np.mean(df)
        derivatives['dm'] = dm
        derivatives['dc'] = dc
        return derivatives

    def update_parameters(self, derivatives, learning_rate):
        self.parameters['m'] = self.parameters['m'] - learning_rate * derivatives['dm']
        self.parameters['c'] = self.parameters['c'] - learning_rate * derivatives['dc']

    def train(self, learning_rate, iters):
        # initialize random parameter between 0 and 1 for m and c as y = mx + c
        m = np.random.uniform(0, 1) * -1
        c = np.random.uniform(0, 1) * -1
        self.parameters['m'] = m
        self.parameters['c'] = c
        # initialize the cost function or loss function
        self.loss = []

        # Initialize figure and axis for animation
        fig, ax = plt.subplots()
        x_vals = np.linspace(min(self.train_input), max(self.train_input), 100)
        line, = ax.plot(x_vals, self.parameters['m'] * x_vals +
                        self.parameters['c'], color='red', label='Regression Line')
        ax.scatter(self.train_input, self.train_output, marker='o',
                color='green', label='Training Data')
        # Set y-axis limits to exclude negative values
        ax.set_ylim(0, max(self.train_output) + 1)

        def update(frame):
            predictions = self.forward_propagation(self.train_input)
            # cost_function
            cost = self.cost_function(predictions, self.train_output)
            # Back propagation
            derivatives = self.backward_propagation(self.train_input,
                                                    self.train_output,
                                                    predictions)
            # Update parameters
            self.update_parameters(derivatives, learning_rate)

            #  Update the regression line
            line.set_ydata(self.parameters['m']
                        * x_vals + self.parameters['c'])
            # Append loss and prin
            self.loss.append(cost)
            self.logger.info("Iteration = {}, Loss = {}".format(frame + 1, cost))
            return line
        # Create animation
        ani = FuncAnimation(fig, update, frames=iters, interval=200, blit=False)
        # Save the animation as a video file (e.g., MP4)
        ani.save('linear_regression_A.gif', writer='ffmpeg')

        plt.xlabel('Input')
        plt.ylabel('Output')
        plt.title('Linear Regression')
        plt.legend()
        # plt.show()
        return self.parameters, self.loss

if __name__ == "__main__":
    linear_regression = Linear_regression()
    linear_regression.reshape_data()
    parameters, loss = linear_regression.train(0.00005, 200)