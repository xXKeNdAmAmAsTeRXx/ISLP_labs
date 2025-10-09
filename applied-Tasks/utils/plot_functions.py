
import matplotlib.pyplot as plt
import numpy as np


def plot_data(trainX, trainY, testX, testY,
                            xlabel='X', ylabel='Y',
                            train_title='Training Data',
                            test_title='Val Data',
                            main_title='Val vs Test Data'):
    """Plot training and test scatter plots side by side."""

    # Handle 2D input (use first feature)
    if trainX.ndim > 1:
        trainX = trainX[:, 0]
    if testX.ndim > 1:
        testX = testX[:, 0]

    # Create figure with 1 row, 2 columns
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # --- Training data plot ---
    axes[0].scatter(trainX, trainY, color='blue', alpha=0.7, edgecolor='k')
    axes[0].set_title(train_title)
    axes[0].set_xlabel(xlabel)
    axes[0].set_ylabel(ylabel)
    axes[0].grid(True)

    # --- Test data plot ---
    axes[1].scatter(testX, testY, color='red', alpha=0.7, edgecolor='k')
    axes[1].set_title(test_title)
    axes[1].set_xlabel(xlabel)
    axes[1].set_ylabel(ylabel)
    axes[1].grid(True)

    # Add an overall title for both plots
    fig.suptitle(main_title, fontsize=14, fontweight='bold')

    # Adjust spacing and show
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


import matplotlib.pyplot as plt

def plot_loss(loss_values, title="Loss over Epochs", xlabel="Epoch", ylabel="Loss", save_path=None):
    """
    Plots the loss values over epochs.

    Parameters:
    - loss_values (list or array): Sequence of loss values.
    - title (str): Title of the plot.
    - xlabel (str): Label for the x-axis.
    - ylabel (str): Label for the y-axis.
    - save_path (str or None): If provided, saves the plot to the given path.
    """
    epochs = range(1, len(loss_values) + 1)
    
    plt.figure(figsize=(8, 5))
    plt.plot(epochs, loss_values, marker=None, linestyle='-', color='r', label='Loss', linewidth=0.8)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    
    plt.show()

def plot_line_on_data(x, y, slope, intercept, title="Linear Fit", xlabel="X", ylabel="Y"):
    """
    Plots a scatter plot of the data and overlays a line with given slope and intercept.
    
    Parameters:
        x (array-like): X data
        y (array-like): Y data
        slope (float): Line slope
        intercept (float): Line intercept
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    


    # Scatter plot of data
    plt.scatter(x, y, color='blue', label='Data Points')
    
    # Line values
    x_line = np.linspace(min(x), max(x), 100)
    y_line = slope * x_line + intercept
    
    # Plot the line
    plt.plot(x_line, y_line, color='red', label=f'Line: y = {slope:.2f}x + {intercept:.2f}')
    
    # Labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_quadratic(a, b, c, x, y):
    """
    Plots a quadratic function y = a*x^2 + b*x + c along with scatter points.

    Parameters:
    a, b, c : coefficients of the quadratic function
    x, y    : arrays of data points to scatter
    """
    # Scatter the given points
    plt.scatter(x, y, color='blue', label='Data points')
    
    # Generate smooth x values for plotting the quadratic curve
    x_curve = np.linspace(min(x), max(x), 500)
    y_curve = a * x_curve**2 + b * x_curve + c
    
    # Plot the quadratic curve
    plt.plot(x_curve, y_curve, color='red', label=f'Quadratic: {a}x² + {b}x + {c}')
    
    # Add labels and legend
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Function with Scatter Points')
    plt.legend()
    plt.show()