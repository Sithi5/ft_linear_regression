import io
import pandas as pd

from src.global_var import THETA_VALUE_FILE_PATH
from pandas.core.frame import DataFrame


def read_csv_file(csv_file_path) -> DataFrame:
    try:
        data = pd.read_csv(csv_file_path)
    except Exception as e:
        print("read_csv_file failed: ", e)
        raise
    return data


def get_theta_values_from_file() -> tuple():
    try:
        with open(THETA_VALUE_FILE_PATH) as file:
            theta = file.read()
            theta = theta.split()
        return (float(theta[0]), float(theta[1]))
    except:
        return (0.0, 0.0)


def write_theta_file(theta_0: float, theta_1: float):
    try:
        with open(THETA_VALUE_FILE_PATH, "w") as file:
            file.write(str(theta_0) + " " + str(theta_1))
    except io.UnsupportedOperation as e:
        print("Write theta file fail: ", e)
        raise
    except Exception as e:
        print("Write theta file fail: ", e)
        raise
