from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Using two itterations to compare numbers to exclude the product of self.
    Overall Time Complexity -> 0(n^2), two itterations
    Overall Space Complexity -> O(n), store the answer array
    """
    lenght = len(nums)
    answer = []
    for first_index in range(lenght):
        product = 1
        for second_index in range(lenght):
            if first_index == second_index:
                continue
            product *= nums[second_index]
        answer.append(product)

    return answer


nums = [7, 1, 4, 6]
print(productExceptSelf(nums))
