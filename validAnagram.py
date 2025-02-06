class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return s == t
    
solution = Solution()

print(solution.isAnagram('anagram', 'nagaram'))  # True
print(solution.isAnagram('rat', 'car'))  # False