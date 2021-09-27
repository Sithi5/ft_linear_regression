# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cli.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mabouce <ma.sithis@gmail.com>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/01 20:27:45 by mabouce           #+#    #+#              #
#    Updated: 2021/09/27 18:31:37 by mabouce          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import click
import pandas as pd
from pandas.core.frame import DataFrame
from pathlib import Path

from src.global_var import DEFAULT_CSV_FILE_PATH, THETA_VALUE_FILE_PATH
from src.print import print_data
from src.deep_learner import DeepLearner
from src.utils import write_theta_file


def read_csv_file(csv_file_path) -> DataFrame:
    data = pd.read_csv(csv_file_path)
    print_data(data=data)
    return data


def get_theta_values() -> tuple():
    try:
        with open(THETA_VALUE_FILE_PATH) as file:
            theta = file.read()
            theta = theta.split()
        return (float(theta[0]), float(theta[1]))
    except:
        return (0.0, 0.0)


@click.command()
@click.argument(
    "km",
    type=float,
)
def predict(km: float):
    try:
        theta_0, theta_1 = get_theta_values()
        predicted_price = theta_0 + theta_1 * km
        print("The estimated price of the car is : ", predicted_price)
    except:
        print("predict failed.")


@click.command()
@click.option("-d", "--debug", default=False, help="Add debug message")
@click.argument(
    "file_data_path",
    default=DEFAULT_CSV_FILE_PATH,
    type=click.Path(exists=True, readable=True, path_type=Path),
)
def learn(file_data_path: Path, debug: bool):
    try:
        deep_learner = DeepLearner()
        deep_learner.learn()
    except:
        print("learning failed.")


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
