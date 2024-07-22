from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Given an array of integers that was originally sorted in ascending order and is possibly
        rotated at an unknown pivot. For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
    Using modifing binary search in a rotated sorted array to determine which part of the array
        is properly sorted to adjust the binary search accordingly.
    Time complexity: O(log(n)), complexity of binary search.
    Space Complexity: O(1), store only constant
    """
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums=nums, target=target))
