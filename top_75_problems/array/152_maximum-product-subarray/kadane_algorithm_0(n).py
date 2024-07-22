from typing import List


def maxProduct(nums: List[int]) -> int:
    """
    Traverse the array from both side, the prefix starts from beginning, the sufix from ending.
        At each step, update the prefix and suffix products and then compare them with the
            current max_product to update. If prefix and siffix becomes zero, reset to 1.
    Time complexity: O(n), one itteration.
    Space Complexity: 0(1), store only constant.
    """
    prefix, suffix = 1, 1
    max_product = -float("inf")
    for idx in range(len(nums)):
        prefix *= nums[idx]
        suffix *= nums[~idx]
        max_product = max(max_product, prefix, suffix)

        # prefix = prefix or 1 is used to assign a default value to the variable prefix
        #   if prefix is considered "falsy." => 0 or 1 => 1, not product with 0.
        prefix = prefix or 1
        suffix = suffix or 1
    return max_product


nums = [2, 3, -2, 4]
print(maxProduct(nums))
