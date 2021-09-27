from src.global_var import THETA_VALUE_FILE_PATH
import io


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
