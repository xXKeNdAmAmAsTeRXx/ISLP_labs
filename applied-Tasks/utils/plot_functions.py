
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

