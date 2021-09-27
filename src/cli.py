# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cli.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mabouce <ma.sithis@gmail.com>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/01 20:27:45 by mabouce           #+#    #+#              #
#    Updated: 2021/09/27 17:09:20 by mabouce          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import click
import argparse
import pandas as pd
from pandas.core.frame import DataFrame
from typing import Tuple
from pathlib import Path

from src.global_var import DEFAULT_CSV_FILE_PATH
from src.print import print_data


def read_csv_file(csv_file_path) -> DataFrame:
    data = pd.read_csv(csv_file_path)
    print_data(data=data)
    return data


def get_theta_values():
    return (0.0, 0.0)


@click.command()
def predict(km: float = 0):
    theta_0, theta_1 = get_theta_values()
    return theta_0 + theta_1 * km


@click.command()
@click.option("-d", "--debug", default=False, help="Add debug message")
@click.argument(
    "file_data_path",
    default=DEFAULT_CSV_FILE_PATH,
    type=click.Path(exists=True, readable=True, path_type=Path),
)
def learn(file_data_path: Path, debug: bool):
    if debug is False:
        try:
            read_csv_file(csv_file_path=file_data_path)
        except SyntaxError as e:
            print("The expression syntax is not accepted : ", e)
        except ValueError as e:
            print("One of the value in the expression is not accepted : ", e)
        except NotImplementedError as e:
            print("One of the methods needed is not implemented yet : ", e)
        except Exception as e:
            print("An exception appened : ", e)
    else:
        read_csv_file(csv_file_path=file_data_path)


@click.group()
def cli():
    pass


cli.add_command(learn)
cli.add_command(predict)


if __name__ == "__main__":
    cli()
