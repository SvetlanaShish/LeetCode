from typing import List


def maxProduct(nums: List[int]) -> int:
    """
    Check product of every possible array and track of the maximum product.
    Time complexity: O(n^2), nested loops checking.
    Space Complexity: 0(1), store only constant.
    """
    max_product = -float("inf")
    n = len(nums)

    for i in range(n):
        current_product = 1

        for j in range(i, n):
            current_product *= nums[j]
            if current_product > max_product:
                max_product = current_product
            current_product = current_product or 1
    return max_product


nums = [2, 3, -2, 4]
print(maxProduct(nums))
