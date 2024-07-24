from typing import List


def maxArea(height: List[int]) -> int:
    """
    Iterating through all possible pairs of lines, calculating the area for each pair,
        and updating the maximum area found.
    Time complexity: O(n^2), nested loops iterartion.
    Space Complexity: O(1), store only constant.
    """
    n = len(height)
    max_area = 0
    for i in range(n - 1):
        if not height[i]:
            continue
        for j in range(i, n):
            if not height[j]:
                continue
            current_area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, current_area)
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
