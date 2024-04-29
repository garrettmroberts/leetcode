class Solution:
    def isPalindrome(self, s: str) -> bool:
        test_str = []
        for ch in s:
            if ch.isalnum():
                test_str.append(ch)
        test_str = "".join(test_str).lower()
        return test_str == test_str[::-1]
