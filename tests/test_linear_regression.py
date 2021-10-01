import pytest

from src.global_var import DEFAULT_CSV_FILE_PATH
from src.deep_learner import DeepLearner
from src.utils import (
    delete_info_file,
    save_info_to_file,
    get_info_from_file,
    read_csv_file,
    delete_info_file,
)
from src.cli import predictor


def test_predict():
    try:
        delete_info_file()
    except:
        pass
    km = 15000
    predicted_price = predictor(km=km)
    # No learning yet, should predict price 0.0
    assert predicted_price == 0.0
    data = read_csv_file(csv_file_path=DEFAULT_CSV_FILE_PATH)
    deep_learner = DeepLearner()
    deep_learner.learn_with_linear_regression(data=data.copy())
    predicted_price = predictor(km=km)
    assert predicted_price != 0.0


def test_subject():
    data = read_csv_file(csv_file_path=DEFAULT_CSV_FILE_PATH)

    deep_learner = DeepLearner()
    deep_learner.learn_with_linear_regression(data=data.copy())

    m = len(data)
    x = data.iloc[0:m, 0]
    y = data.iloc[0:m, 1]

    max_diff = 0
    max_diff_km = -1
    average_diff = 0
    for index in range(m):
        km = x[index]
        real_price = y[index]
        predicted_price = predictor(km=km)
        diff = abs(int(real_price) - int(predicted_price))
        print("km=\t\t\t", km)
        print("predicted_price=\t", int(predicted_price))
        print("real_price=\t\t", int(real_price))
        print("diff =\t\t\t", diff)
        print()
        if diff > max_diff:
            max_diff = diff
            max_diff_km = km
        average_diff += diff
    average_diff /= m
    print()
    print("The average diff value is: ", average_diff)

    if max_diff_km > 0:
        print(
            "The biggest diff is for ",
            str(int(max_diff_km)),
            "km with a value of: ",
            max_diff,
        )
