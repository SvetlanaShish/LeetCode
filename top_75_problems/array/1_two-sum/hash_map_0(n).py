from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Hash map uses to store numbers and indexes of nums. If the second number in hash map => return index of second
        number and index of current element.
    Time Complexity: 0(n), because each lookup and insertion in the dictionary is O(1).
    Space Complexity: 0(n), due to the additional storage in the dictionary.
    """
    num_map = {}
    for idx, element in enumerate(nums):
        second_number = target - element
        if second_number in num_map:
            return [num_map[second_number], idx]
        num_map[element] = idx


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
