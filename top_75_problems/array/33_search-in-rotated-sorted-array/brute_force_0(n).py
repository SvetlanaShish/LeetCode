from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Itterate through an array and compare elements with target. If element equal to target,
        return it's value.
    Time complexity: O(n), one itteration.
    """
    for index, num in enumerate(nums):
        if num == target:
            return index
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums=nums, target=target))
