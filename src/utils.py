import io
import pandas as pd
from numpy.typing import ArrayLike

from src.global_var import THETA_VALUE_FILE_PATH
from pandas.core.frame import DataFrame


def read_csv_file(csv_file_path) -> DataFrame:
    """
    This function read a csv file from the input path and return a DataFrame object.
    """
    try:
        data = pd.read_csv(csv_file_path)
    except Exception as e:
        print("read_csv_file failed: ", e)
        raise
    return data


def get_theta_values_from_file() -> tuple():
    """
    This function read the theta values contained in the file and return it.
    If the file doesn't exist, it will return 0.0 0.0 as default value.
    """
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
    except Exception as e:
        print("Write theta file fail: ", e)
        raise


def maximum_absolute_scaling(data_frame: DataFrame):
    # Copy the dataframe
    data_frame_scaled = data_frame.copy()
    # Apply maximum absolute scaling
    for column in data_frame_scaled.columns:
        data_frame_scaled[column] = (
            data_frame_scaled[column] / data_frame_scaled[column].abs().max()
        )
    return data_frame_scaled
