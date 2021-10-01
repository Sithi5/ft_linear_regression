# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cli.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mabouce <ma.sithis@gmail.com>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/01 20:27:45 by mabouce           #+#    #+#              #
#    Updated: 2021/10/01 15:24:43 by mabouce          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import click
from pathlib import Path

from src.global_var import DEFAULT_CSV_FILE_PATH
from src.deep_learner import DeepLearner
from src.utils import save_info_to_file, get_info_from_file, read_csv_file


def predictor(km: float) -> float:
    """
    This function predict the price of a car using the info saved by the learning method, and return the predicted price.
    """
    try:
        original_data_scale, theta_0, theta_1 = get_info_from_file()

        if theta_0 == 0 and theta_1 == 0:
            print("The model is not trained.")
            return 0.0
        # Put km into the normalized scale
        km /= original_data_scale
        predicted_price = theta_0 + theta_1 * km
        # Put back the price to normal scale
        return predicted_price * original_data_scale
    except:
        print("predictor failed.")
        raise


@click.command()
@click.argument(
    "km",
    type=float,
)
def predict(km: float):
    """
    Command to predict price of a car with the input km.
    """
    try:
        predicted_price = predictor(km=km)
        print("The estimated price of the car is : ", predicted_price)
    except:
        pass


@click.command()
@click.argument(
    "csv_file_path",
    default=DEFAULT_CSV_FILE_PATH,
    type=click.Path(exists=True, readable=True, path_type=Path),
)
def learn(csv_file_path: Path):
    """
    This function will train the model and set theta_0 and theta_1.
    """
    # try:
    data = read_csv_file(csv_file_path=csv_file_path)
    if data.empty:
        print("data is empty, nothing to learn.")
        return
    deep_learner = DeepLearner()
    deep_learner.learn_with_linear_regression(data=data.copy())
    # except:
    # print("learning failed.")


@click.argument(
    "theta_1",
    type=float,
)
@click.argument(
    "theta_0",
    type=float,
)
@click.command()
def set_theta(theta_0: float, theta_1: float):
    """
    Set manually the thetas.
    """
    try:
        save_info_to_file(original_data_scale=1.0, theta_0=theta_0, theta_1=theta_1)
        print("new theta set to: ", str(theta_0) + " " + str(theta_1))
    except:
        print("set theta failed.")


@click.group()
def cli():
    pass


cli.add_command(learn)
cli.add_command(predict)
cli.add_command(set_theta)


if __name__ == "__main__":
    print()
    cli()
