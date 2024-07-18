from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Calculate the prefix product and the suffix product for all the values except self and
        combine this results.
    Example:
        nums   = [     7,          1,             4,       6    ]
        answer = [( | 1*4*6), ( 7 | 4*6), ( 7*1 | 6),  (7*1*4) | ]
        
    Overall Time Complexity -> 0(n) for range(n)
    Overall Space Complexity -> O(n) and O(1) extra space complexity, as the algorithm
        only uses a constant amount of extra space (excluding the output array).
    """
    n = len(nums)
    answer = [1] * n

    left_product = 1
    for i in range(n):
        answer[i] *= left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer


nums = [7, 1, 4, 6]
print(productExceptSelf(nums))
