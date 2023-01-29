from typing import List


class Pairer:
    def __init__(self, values: List[int], target: int):
        self._values = values
        self._target = target

    def count_nums(self, values):
        counter = {}
        for key in values:
            if key in counter:
                counter[key] = counter[key] + 1
            else:
                counter[key] = 1
        return counter

    def compute(self) -> List[List[int]]:
        pairs = []
        counter = self.count_nums(self._values)
        for key, value in counter.items():
            missing_number = self._target - key
            count_missing_numbers = counter.get(missing_number, 0)
            for _ in range(min(value, count_missing_numbers)):
                # Unique numbers in a pair.
                if key != missing_number:
                    pairs.append(sorted([key, missing_number]))
                    counter[key] -= 1
                    counter[missing_number] -= 1
                # Duplicate numbers in pair.
                elif value > 1 and key == missing_number:
                    pairs.append([key, missing_number])
                    counter[key] -= 1
                    counter[missing_number] -= 1
                    value -= 2
        return pairs
