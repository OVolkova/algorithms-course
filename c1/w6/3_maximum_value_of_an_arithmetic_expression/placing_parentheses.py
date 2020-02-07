# Uses python3
import numpy as np

OPERATIONS = {'+', '-', '*'}


class MaximumParentheses:
    def __init__(self, line, oprations):
        self.objects, self.operations = self.split_input(line, oprations)
        self.maximums = np.diag(self.objects)
        self.minimums = np.diag(self.objects)
        self.fill_maximums_minimums_values()
        self.maximum_value = self.maximums[0, len(self.objects)-1]

    @staticmethod
    def split_input(line, operations):
        prev = 0
        objects = []
        ops = []
        for i, elem in enumerate(line):
            if elem in operations:
                objects.append(int(line[prev:i]))
                ops.append(line[i])
                prev = i + 1
        objects.append(int(line[prev:]))
        return objects, ops

    @staticmethod
    def evalt(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            assert False

    def get_min_and_max(self, first, second):
        min_value = None
        max_value = None
        for i in range(first, second):
            max_max = self.evalt(self.maximums[first, i], self.maximums[i+1, second], self.operations[i])
            max_min = self.evalt(self.maximums[first, i], self.minimums[i+1, second], self.operations[i])
            min_max = self.evalt(self.minimums[first, i], self.maximums[i+1, second], self.operations[i])
            min_min = self.evalt(self.minimums[first, i], self.minimums[i+1, second], self.operations[i])
            if min_value:
                min_value = min(min_value, max_max, max_min, min_max, min_min)
            else:
                min_value = min(max_max, max_min, min_max, min_min)
            if max_value:
                max_value = max(max_value, max_max, max_min, min_max, min_min)
            else:
                max_value = max(max_max, max_min, min_max, min_min)
        return min_value, max_value

    def fill_maximums_minimums_values(self):
        for s in range(1, len(self.objects)):
            for i in range(0, len(self.objects)-s):
                j = i + s
                self.minimums[i, j], self.maximums[i, j] = self.get_min_and_max(i, j)


if __name__ == "__main__":
    print(MaximumParentheses(input(), OPERATIONS).maximum_value)
