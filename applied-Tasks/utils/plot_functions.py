
import matplotlib.pyplot as plt

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
