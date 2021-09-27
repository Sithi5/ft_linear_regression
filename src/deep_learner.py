from src.utils import write_theta_file


class DeepLearner:
    def __init__(self):
        self._theta_0 = 0.0
        self._theta_1 = 0.0

    def learn(self):
        self._theta_0 = 10.0
        self._theta_1 = 5.0
        write_theta_file(theta_0=self._theta_0, theta_1=self._theta_1)
