from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Check all possible triplets in the array to see if they sum to zero, and sort triplet to avoid
        duplicates.
    Time complexity: O(n^3), three nested loops to check every combination of triplets.
    Space Complexity: O(1), store only constant (excluding the space required for the output).
    """

    triplets = []
    n = len(nums)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted(
                        [nums[i], nums[j], nums[k]]
                    )  # Sort the triplet to avoid duplicates
                    if triplet not in triplets:
                        triplets.append(triplet)
    return triplets


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
