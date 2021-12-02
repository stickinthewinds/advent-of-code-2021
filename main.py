#!/usr/bin/env python3

from datetime import datetime
import sys
import argparse
from day import *

# Current day number
today = datetime.now().today().day

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="input file", nargs='?', default="input.txt", const="input.txt")
parser.add_argument("-d", "--day", type=int, help="day number", nargs='?', default=today, const=today)


def day_to_class(day: str):
    return getattr(sys.modules[__name__], day)


def main(args):
    try:
        day = f"Day{args.day:02}"
        with open(f"{day}/{args.input}", "r") as f:
            dayClass = day_to_class(day)(f)
            dayClass.task()
    except FileNotFoundError:
        print("'" + args.input + "' doesn't exist.")


if __name__ == "__main__":
    main(parser.parse_args())
