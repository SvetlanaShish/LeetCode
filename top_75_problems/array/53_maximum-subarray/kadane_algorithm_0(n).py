from typing import List


def maxSubArray(nums: List[int]) -> int:
    """
    Itterate through array and for each element in array update current_max to be the maximum
        of the current subarray alone or the current element + current_max. Update overall_max.
    Time complexity: O(n), one itteration.
    Space Complexity: 0(1), store only constant.
    """
    current_max = 0
    overall_max = -float("inf")
    for num in nums:
        current_max = max(current_max + num, num)
        overall_max = max(overall_max, current_max)
    return overall_max


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
