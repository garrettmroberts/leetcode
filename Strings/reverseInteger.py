class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        listed = list(str(abs(x)))
        l, r = 0, len(listed) - 1
        for i in range(len(listed) // 2):
            listed[l], listed[r] = listed[r], listed[l]
            l += 1
            r -= 1

        res = int("".join(listed))
        if res < -(2**31) or res > 2**31 - 1:
            return 0
        return res * -1 if is_negative else res
