from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        for perm in permutations(digits, 3):
            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            if num % 2 == 0 and perm[0] != 0:
                result.add(num)
        return sorted(result)
