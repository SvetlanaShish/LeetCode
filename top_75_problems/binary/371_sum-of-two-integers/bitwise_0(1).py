def getSum(a: int, b: int) -> int:
    """
    Using bitwise operations to add two integers and ensures that the result fits within
        a 32-bit signed integer range.
    Time complexity: O(1), constant time, since the number of bits is fixed.
    Space Complexity: O(1), constant space.
    """
    mask = 0xFFFFFFFF
    # Iterate till there is no carry
    while mask & b > 0:
        # Calculate carry
        carry = a & b
        # Sum without carry
        a = a ^ b
        # Shift carry to the left by one to add it in the next iteration
        b = carry << 1
    return (a & mask) if b > 0 else a


a = 1
b = 2
print(getSum(1, 2))
