def hammingWeight(n: int) -> int:
    """
    Repeatedly flipping the least significant '1' bit of the number to '0' and
        counting how many times this operation is performed.
    Time complexity: O(k), loop runs exactly as many times as there are '1' bits in n (i.e. k)
    Space Complexity: O(1), constant space.
    """
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count


n = 11
print(hammingWeight(n))
