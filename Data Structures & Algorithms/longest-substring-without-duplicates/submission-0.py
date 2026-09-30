class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        we;re given a string, and we need to find how many unique characters there are.
        we only need to find the value of unique charcters inside of the array
        
        we need to use the sliding window
        """
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res