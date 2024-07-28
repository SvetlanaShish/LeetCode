from typing import List


def countBits(n: int) -> List[int]:
    """
    Checking each bit of each number from 0 to n to count the number of 1s. For each number from
        0 to n, iterate through its bits and count the number of 1s. Store the count of 1s for
            each number in the result array.
    Time complexity: 0(nlog(n)), one loop iteration.
    Space Complexity: 0(n), to store the result array.
    """
    result = []
    for i in range(n + 1):
        count = 0
        num = i
        while num > 0:
            count += num & 1  # Check if the least significant bit is 1
            num >>= 1  # Right shift by 1 bit
        result.append(count)
    return result


n = 2
print(countBits(2))
