from typing import List


def maxArea(height: List[int]) -> int:
    """
    Initializing two pointers at the beginning and end of the array, calculating the container area,
        updating the maximum area found, and moving the pointer pointing to the shorter line inward
            until the pointers meet.
    Time complexity: O(n), because each pointer moves at most n times.
    Space Complexity: O(1), store only constant.
    """
    n = len(height)
    max_area = 0
    left, right = 0, n - 1
    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
