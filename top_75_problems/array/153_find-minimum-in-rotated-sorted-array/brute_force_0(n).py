from typing import List


def findMin(nums: List[int]) -> int:
    """
    Itterate through an array and compare all elements to find the minimum.
    Time complexity: O(n), one itteration.
    Space Complexity: O(1), store only constant.
    """
    min_value = float("inf")
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value


nums = [3, 4, 5, 1, 2]
print(findMin(nums))
