from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    """
    Use set to keep track of the elements in nums. Itterate through the array to check if the 
        current element is in set.
    Time complexity: 0(n), one itteration is the most expensive operation.
    Space Complexity: O(n), store list of seen nums in most worst case.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
