from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Check all possible pairs, we need to check two loops which is 0(n^2).
    Time complexity: 0(n^2), two times itteration.
    Space Complexity: 0(1), does not use any additional data structure to store.
    """
    for index_first, first_num in enumerate(nums):
        for index_second, second_num in enumerate(nums):
            if index_first == index_second:
                break
            if (first_num + second_num) == target:
                return [index_first, index_second]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
