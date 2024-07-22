from typing import List


def maxSubArray(nums: List[int]) -> int:
    """
    Check sum of every possible array and track of the maximum sum.
    Time complexity: O(n^2), nested loops checking.
    Space Complexity: 0(1), store only constant.
    """
    max_sum = -float("inf")
    n = len(nums)

    for i in range(n):
        current_sum = 0

        for j in range(i, n):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
