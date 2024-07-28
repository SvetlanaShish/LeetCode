from typing import List


def countBits(n: int) -> List[int]:
    """
    Dynamic programming - the number of '1' bits in a number i can be derived from the number
        of '1' bits in a smaller number. If we know the number of '1' bits in i // 2
            (which is i >> 1), we can derive the number of '1' bits in i based on whether
                i is even or odd:
                    - even, ans[i] = ans[i >> 1]
                    - odd, ans[i] = ans[i >> 1] + 1
    Time complexity: 0(n), one loop iteration.
    Space Complexity: 0(n), additional space (n+1).
    """
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


n = 2
print(countBits(2))
