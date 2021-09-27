# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mabouce <ma.sithis@gmail.com>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/01 20:27:45 by mabouce           #+#    #+#              #
#    Updated: 2021/09/27 11:16:19 by mabouce          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse


# from src.expression_resolver import ExpressionResolver
# from gui.app import Application
# from src.assignment.assigned_file import clear_assigned_file, list_assigned_file


def main(argv=None):
    print()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        help="Add verbose and print different resolving step.",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="Remove exception catching.",
        action="store_true",
    )
    args = parser.parse_args(argv)


if __name__ == "__main__":
    main()
