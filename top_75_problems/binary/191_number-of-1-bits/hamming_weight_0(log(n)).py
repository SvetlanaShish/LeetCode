def hammingWeight(n: int) -> int:
    """
    Use the bitwise AND operation (&) to check the least significant bit (LSB)
        and then shift the number to the right until all bits have been checked.
    Time complexity: O(log(n)), loop runs as long as there are bits in n, which is proportional to the number
        of bits in the binary representation of n.
    Space Complexity: O(1), constant space.
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


n = 11
print(hammingWeight(n))
