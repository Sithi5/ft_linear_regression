import os
import matplotlib.pyplot as plt

from numpy.typing import ArrayLike
from pandas.core.frame import DataFrame

from src.global_var import RESOURCES_DIR_PATH


def print_data(data: DataFrame):
    print("\tDATA")
    print("==================================================")
    print(data)
    print("==================================================")


def scatter_plot_graph(
    X: ArrayLike,
    Y: ArrayLike,
    xlabel: str = None,
    ylabel: str = None,
    to_show: bool = False,
    to_save: bool = True,
    title: str = None,
):
    """
    Use mathplot to create a scatter plot graph. The graph can be show or saved.
    """
    axes = plt.axes()
    axes.grid()  # Draw a grid
    plt.scatter(X, Y)
    plt.title(label=title)
    plt.xlabel(xlabel=xlabel)
    plt.ylabel(ylabel=ylabel)
    if to_show is True:
        plt.show()
    if to_save is True:
        plt.savefig(os.path.join(RESOURCES_DIR_PATH, title + ".png"))
