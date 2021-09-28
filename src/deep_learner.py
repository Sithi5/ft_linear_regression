from pandas.core.frame import DataFrame

from src.utils import write_theta_file, get_theta_values_from_file


class DeepLearner:
    def __init__(self):
        try:
            self._theta_0, self._theta_1 = get_theta_values_from_file()
        except:
            self._theta_0 = 0.0
            self._theta_1 = 0.0

    def learn(self, data: DataFrame):
        try:
            print("new theta set to: ", str(self._theta_0) + " " + str(self._theta_1))
            write_theta_file(theta_0=self._theta_0, theta_1=self._theta_1)
        except Exception as e:
            print("DeepLearner learn failed: ", e)
            raise
