import math
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        if n==2:
            return [1,2]
        previous_n0 = math.inf
        previous_n1 = math.inf
        for i in range(n):
            if numbers[i] == previous_n0:
                continue
            previous_n0 = numbers[i]
            previous_n1 = math.inf
            for j in range(i+1,n):
                if numbers[j] == previous_n1:
                    continue
                if target == numbers[i] + numbers[j]:
                    return [i+1,j+1]
                previous_n1 = numbers[j]