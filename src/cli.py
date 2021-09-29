# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cli.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mabouce <ma.sithis@gmail.com>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/01 20:27:45 by mabouce           #+#    #+#              #
#    Updated: 2021/09/29 16:50:56 by mabouce          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import click
from pathlib import Path

from src.global_var import DEFAULT_CSV_FILE_PATH, THETA_VALUE_FILE_PATH
from src.print import print_data
from src.deep_learner import DeepLearner
from src.utils import write_theta_file, get_theta_values_from_file, read_csv_file


@click.command()
@click.argument(
    "km",
    type=float,
)
def predict(km: float):
    """
    Predict price of a car with the input km.
    """
    try:
        theta_0, theta_1 = get_theta_values_from_file()
        if theta_0 == 0 and theta_1 == 0:
            print("The model is not trained.")
            return
        predicted_price = theta_0 + theta_1 * km
        print("The estimated price of the car is : ", predicted_price)
    except:
        print("predict failed.")


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
    deep_learner.learn_with_linear_regression(data=data)
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
        write_theta_file(theta_0=theta_0, theta_1=theta_1)
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
