#!/usr/bin/env python3

import sys

def calc_window_sum(nums: list[int]):
    return sum(nums)


def task(lines: list[int], window: int=1):
    numLines = len(lines)
    if numLines < 1 or numLines == 1 or numLines <= window:
        return 0
    count = 0
    current = calc_window_sum(lines[0:window])
    for i in range(1, numLines):
        nextSum = calc_window_sum(lines[i:i + window])
        if nextSum > current:
            count += 1
        current = nextSum
    return count


def main(args):
    if len(args) < 1:
        file = "input.txt"
    else:
        file = args[0]
    try:
        with open(file, "r") as f:
            lines = [int(x) for x in f]
            print(task(lines))
            print(task(lines, 3))
    except FileNotFoundError:
        print("'" + args[0] + "' doesn't exist.")


if __name__ == "__main__":
    main(sys.argv[1:])
