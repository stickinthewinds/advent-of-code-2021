from abc import ABC, abstractmethod


# Override for the current day
class Day(ABC):
    def __init__(self, lines: list[str]):
        self.lines = lines

    def lines_as_int(self):
        return [int(x) for x in self.lines]

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
        a = self.lines_as_int()
        print(self.perform_task(a))
        print(self.perform_task(a, 3))

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


class Day03(Day):
    def calc_binary(self, num: str):
        position = 0
        total = 0
        for c in num[::-1]:
            if c == "1":
                total += pow(2, position)
            position += 1
        return total

    def greatest_bit(self, lines: list[int], position: int=0):
        curr = 0
        for n in lines:
            if n[position] == "1":
                curr += 1
            else:
                curr -= 1
        return curr

    def part1(self):
        buckets = [0] * (self.lineLength)
        for c in range(0, self.lineLength):
            buckets[c] = 1 if self.greatest_bit(self.lines, c) > 0 else 0
        gamma = ""
        epsilon = ""
        for b in buckets:
            if b > 0:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"
        g = self.calc_binary(gamma)
        e = self.calc_binary(epsilon)
        print(g * e)

    def calc_rating(self, nums: list[str], p: int=0, common: bool=True):
        if (len(nums) == 1):
            return nums
        b = self.greatest_bit(nums, p)
        if b > 0:
            b = 1
        elif b < 0:
            b = 0
        else:
            b = 1
        if not common:
            if b == 1:
                b = 0
            else:
                b = 1
        return self.calc_rating([l for l in nums if int(l[p]) == b], (p + 1) % self.lineLength, common)

    def part2(self):
        position = 0
        o = self.calc_rating(self.lines)
        c = self.calc_rating(self.lines, common=False)
        oBin = self.calc_binary(o[0])
        cBin = self.calc_binary(c[0])
        print(oBin * cBin)

    def task(self):
        self.lineLength = len(self.lines[0])

        self.part1()
        self.part2()
