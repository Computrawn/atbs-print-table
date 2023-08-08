#!/usr/bin/env python3
# print_table.py — An exercise in manipulating strings.
# For more information, see README.md

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.

table_data_1: list[str] = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

table_data_2: list[str] = [
    ["apples", "oranges", "cherries", "banana", "kiwi"],
    ["Alice", "Bob", "Carol", "David", "Barbara"],
    ["dogs", "cats", "moose", "goose", "giraffe"],
]


def main():
    print_table(table_data_1)
    print()
    print_table(table_data_2)


def print_table(data: list[str]) -> None:
    col_widths = [0] * len(data)
    for row in range(len(data)):
        lengths = []
        for column in range(len(data[row])):
            lengths.append(len(data[row][column]))
            col_widths[row] = sorted(lengths)[-1]
    for i in range(len(data[row])):
        print(
            f"{data[0][i].rjust(col_widths[0])} | {data[1][i].rjust(col_widths[1])} | {data[2][i].rjust(col_widths[2])}"
        )


if __name__ == "__main__":
    main()
