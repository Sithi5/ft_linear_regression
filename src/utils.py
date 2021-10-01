import os
import pandas as pd

from src.global_var import SAVE_FILE_PATH
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


def get_info_from_file() -> tuple():
    """
    This function read the originial_data_scale and the theta values contained in the file and return it as a tuple.
    If the file doesn't exist, it will return (1.0, 0.0, 0.0) as default value.
    """
    try:
        with open(SAVE_FILE_PATH) as file:
            infos = file.read()
            infos = infos.split()
        return (float(infos[0]), float(infos[1]), float(infos[2]))
    except:
        return (1.0, 0.0, 0.0)


def save_info_to_file(original_data_scale: float, theta_0: float, theta_1: float):
    """
    Save originial_data_scale, the two theta value into a file save_info.
    """
    try:
        with open(SAVE_FILE_PATH, "w") as file:
            file.write(str(original_data_scale) + " " + str(theta_0) + " " + str(theta_1))
        print("Saved into file following datas : ")
        print("\toriginal_data_scale : \t", original_data_scale)
        print("\ttheta_0 : \t\t", theta_0)
        print("\ttheta_1 : \t\t", theta_1)
    except Exception as e:
        print("Write save_info file fail: ", e)
        raise


def delete_info_file():
    """
    Delete save_info file.
    """
    try:
        os.remove(SAVE_FILE_PATH)
    except Exception as e:
        print("Delete save_info file fail: ", e)
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
