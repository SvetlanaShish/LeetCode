from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Sort array to avoid duplicates in triplets and then using two pointers technique adjust
        them depending on he sum of the triplet.
    Time complexity: O(n^2), each iteration of the for loop involves a two-pointer scan.
    Space Complexity: O(1), store only constant (excluding the space required for the output).
    """

    triplets = []
    nums.sort()
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                triplets.append([nums[i], nums[j], nums[k]])
                j += 1

                # avoid duplicates for left pointer
                while nums[j] == nums[j - 1] and j < k:
                    j += 1
    return triplets


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
