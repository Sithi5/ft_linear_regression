import os
import matplotlib.pyplot as plt

from numpy.typing import ArrayLike
from pandas.core.frame import DataFrame

from src.utils import write_theta_file, get_theta_values_from_file, maximum_absolute_scaling
from src.global_var import RESOURCES_DIR_PATH


class DeepLearner:
    """
    This class use input data to learn with different methods.
    """

    def __init__(self):
        try:
            self._theta_0, self._theta_1 = get_theta_values_from_file()
        except:
            self._theta_0 = 0.0
            self._theta_1 = 0.0

    def _linear_regression_learn_theta_0(self):
        learning_ratio = 1
        return learning_ratio

    def _linear_regression_model(self, x: float):
        # f(x) = ax + b
        return self._theta_0 + self._theta_1 * x

    def _linear_regression_cost(
        self, m: float, x: ArrayLike, y: ArrayLike, learning_ratio: float = 0.5
    ):
        self._theta_0 = (
            learning_ratio
            * (1 / m)
            * sum([(self._linear_regression_model(x[i]) - y[i]) for i in range(m)])
        )
        self._theta_1 = (
            learning_ratio
            * (1 / m)
            * sum([((self._linear_regression_model(x[i]) - y[i]) * x[i]) for i in range(m)])
        )

    def _linear_regression_minimising_cost(self, x: float):
        pass

    def print_linear_regression_model_and_data(
        self,
        x: ArrayLike,
        y: ArrayLike,
        xlabel: str = None,
        ylabel: str = None,
        to_show: bool = False,
        to_save: bool = True,
        title: str = None,
    ):
        """
        Use mathplot to create a scatter plot graph. The graph can be show or saved.
        """
        plt.clf()
        axes = plt.axes()
        axes.grid()  # Draw a grid
        plt.title(label=title)
        plt.xlabel(xlabel=xlabel)
        plt.ylabel(ylabel=ylabel)
        plt.plot(x, y, "r.", label="Data")
        plt.plot(x, self._theta_0 + self._theta_1 * x, "-r", label="regression")
        # f(x) = a + bx
        if to_show is True:
            plt.show()
        if to_save is True:
            plt.savefig(os.path.join(RESOURCES_DIR_PATH, title + ".png"))

    def learn_with_linear_regression(
        self,
        data: DataFrame,
    ):
        """
        Use a pandas module DataFrame object to learn with a linear regression algorithm.
        """

        # try:

        self._theta_0 = 0.0
        self._theta_1 = 0.0

        m = len(data)
        # Select first row of our dataset (km)
        x = data.iloc[0:m, 0]
        # Select second row of our dataset (price)
        y = data.iloc[0:m, 1]

        data = maximum_absolute_scaling(data)
        normalized_x = data.iloc[0:m, 0]
        normalized_y = data.iloc[0:m, 1]

        self.print_linear_regression_model_and_data(
            x=x,
            y=y,
            xlabel="km",
            ylabel="price",
            title="linear_regression_model_and_data_before_learn",
            to_show=False,
        )
        self._linear_regression_cost(m=m, x=x, y=y)

        self.print_linear_regression_model_and_data(
            x=x,
            y=y,
            xlabel="km",
            ylabel="price",
            title="linear_regression_model_and_data_after_learn",
            to_show=False,
        )

        print("new theta set to: ", str(self._theta_0) + " " + str(self._theta_1))
        write_theta_file(theta_0=self._theta_0, theta_1=self._theta_1)
        # except Exception as e:
        #     print("DeepLearner learn failed: ", e)
        #     raise
