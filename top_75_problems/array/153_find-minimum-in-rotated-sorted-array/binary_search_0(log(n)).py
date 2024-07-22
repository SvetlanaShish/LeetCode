from typing import List


def findMin(nums: List[int]) -> int:
    """
    Given an array of integers that was originally sorted in ascending order and is possibly
        rotated at an unknown pivot. For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
    Using modifing binary search in a rotated sorted array, one of the halves will always be sorted,
        and the minimum element will lie in the unsorted half.
    Time complexity: O(log(n)), complexity of binary search.
    Space Complexity: O(1), store only constant
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


nums = [3, 4, 5, 1, 2]
print(findMin(nums))
