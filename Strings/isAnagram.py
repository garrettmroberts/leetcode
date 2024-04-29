class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for char in s:
            location = ord(char) - 97
            if count[location] > 0:
                count[location] = count[location] + 1
            else:
                count[location] = 1

        for char in t:
            location = ord(char) - 97
            count[location] -= 1

        for i in count:
            if i != 0:
                return False

        return True
