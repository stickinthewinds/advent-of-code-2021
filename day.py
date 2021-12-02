from abc import ABC, abstractmethod


# Override for the current day
class Day(ABC):
    def __init__(self, lines: list[str]):
        self.lines = lines

    @abstractmethod
    def task(self):
        pass


class Day01(Day):
    def perform_task(self, intLines: list[int], window: int=1):
        numLines = len(intLines)
        if numLines < 1 or numLines == 1 or numLines <= window:
            return 0
        count = 0
        current = self.calc_window_sum(intLines[0:window])
        for i in range(1, numLines):
            nextSum = self.calc_window_sum(intLines[i:i + window])
            if nextSum > current:
                count += 1
            current = nextSum
        return count

    def task(self):
        intLines = [int(x) for x in self.lines]
        print(self.perform_task(intLines))
        print(self.perform_task(intLines, 3))

    def calc_window_sum(self, nums: list[int]):
        return sum(nums)


class Day02(Day):
    def part1(self, inputs):
        aim = 0
        hPos = 0
        depth = 0
        for i in inputs:
            d = i[0]
            m = int(i[1])
            if d == "forward":
                hPos += m
            elif d == "up":
                depth -= m
            elif d == "down":
                depth += m
        print(hPos * depth)

    def part2(self, inputs):
        aim = 0
        hPos = 0
        depth = 0
        for i in inputs:
            d = i[0]
            m = int(i[1])
            if d == "forward":
                hPos += m
                depth += aim * m
            elif d == "up":
                aim -= m
            elif d == "down":
                aim += m
        print(hPos * depth)

    def task(self):
        a = [x.split() for x in self.lines]
        self.part1(a)
        self.part2(a)
