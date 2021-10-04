import os
import matplotlib.pyplot as plt

from numpy.typing import ArrayLike
from pandas.core.frame import DataFrame
from progress.bar import ChargingBar

from src.utils import save_info_to_file
from src.global_var import RESOURCES_DIR_PATH


class DeepLearner:
    """
    This class use input data to learn with linear regression.
    """

    _learning_rate: float = 0.1
    _eps = 0.001  # Stop condition

    def __init__(self):
        self._learning_range = 1000
        self._theta_0 = 0.0
        self._theta_1 = 0.0

    def _model_function(self, km: float) -> float:
        return self._theta_0 + self._theta_1 * km

    def output_linear_regression_model_and_data(
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
        plt.plot(x, self._model_function(km=x), "-r", label="regression")
        # f(x) = a + bx
        if to_show is True:
            plt.show()
        if to_save is True:
            plt.savefig(os.path.join(RESOURCES_DIR_PATH, title + ".png"))

    def _output_learning_process_graph(self, range_index: int):
        """
        Output graph at different learning time.
        """
        if range_index == self._learning_range / 10:
            self.output_linear_regression_model_and_data(
                x=self._normalized_x,
                y=self._normalized_y,
                xlabel="km",
                ylabel="price",
                title="t1_linear_regression_model",
                to_show=False,
            )
        if range_index == self._learning_range / 5:
            self.output_linear_regression_model_and_data(
                x=self._normalized_x,
                y=self._normalized_y,
                xlabel="km",
                ylabel="price",
                title="t2_linear_regression_model",
                to_show=False,
            )
        if range_index == self._learning_range / 2:
            self.output_linear_regression_model_and_data(
                x=self._normalized_x,
                y=self._normalized_y,
                xlabel="km",
                ylabel="price",
                title="t3_linear_regression_model",
                to_show=False,
            )

    def _partial_derivative_calcul(self) -> tuple():
        derivated_theta0 = float(0)
        derivated_theta1 = float(0)

        derivated_theta0 = (
            self._learning_rate
            * (1 / self._m)
            * sum(
                [
                    self._model_function(km=self._normalized_x[i]) - float(self._normalized_y[i])
                    for i in range(self._m)
                ]
            )
        )
        derivated_theta1 = (
            self._learning_rate
            * (1 / self._m)
            * sum(
                [
                    (self._model_function(km=self._normalized_x[i]) - float(self._normalized_y[i]))
                    * float(self._normalized_x[i])
                    for i in range(self._m)
                ]
            )
        )
        return (derivated_theta0, derivated_theta1)

    def _gradient_descent(self):
        current_cost = sum(
            [
                (self._model_function(km=self._normalized_x[i]) * self._maximum_absolute)
                for i in range(self._m)
            ]
        )
        previous_cost = current_cost
        condition = self._eps + 10.0  # Start with condition greater than eps (assumption)

        bar = ChargingBar("Training", max=self._learning_range, suffix="%(percent)d%%")

        i = 0
        while i < self._learning_range and condition > self._eps:
            derivated_theta0, derivated_theta1 = self._partial_derivative_calcul()
            self._theta_0 = self._theta_0 - derivated_theta0
            self._theta_1 = self._theta_1 - derivated_theta1
            bar.next()
            self._output_learning_process_graph(range_index=i)

            current_cost = sum(
                [
                    (self._model_function(km=self._normalized_x[i]) * self._maximum_absolute)
                    for i in range(self._m)
                ]
            )
            condition = abs(previous_cost - current_cost)
            previous_cost = current_cost
            i += 1

        bar.finish()

    def _normalizing_data(self):
        """
        Normalizing data using maximum absolute scaling algorithm.
        """
        self._maximum_absolute = max(self._data["km"].abs().max(), self._data["price"].abs().max())
        self._original_data_scale = self._maximum_absolute
        self._data["km"] = self._data["km"] / self._maximum_absolute
        self._data["price"] = self._data["price"] / self._maximum_absolute

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

        self._data = data

        self._m = len(data)
        self._x = data.iloc[0 : self._m, 0]
        self._y = data.iloc[0 : self._m, 1]
        self._normalizing_data()
        self._normalized_x = data.iloc[0 : self._m, 0]
        self._normalized_y = data.iloc[0 : self._m, 1]

        self.output_linear_regression_model_and_data(
            x=self._normalized_x,
            y=self._normalized_y,
            xlabel="km",
            ylabel="price",
            title="t0_linear_regression_model",
            to_show=False,
        )

        self._gradient_descent()

        self.output_linear_regression_model_and_data(
            x=self._normalized_x,
            y=self._normalized_y,
            xlabel="km",
            ylabel="price",
            title="t4_linear_regression_model",
            to_show=False,
        )

        save_info_to_file(
            original_data_scale=self._original_data_scale,
            theta_0=self._theta_0,
            theta_1=self._theta_1,
        )
        # except Exception as e:
        #     output("DeepLearner learn failed: ", e)
        #     raise
