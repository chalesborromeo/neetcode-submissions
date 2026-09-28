class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ### an anagram is when two string contain the exact same characters, but the two strings are different words

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)