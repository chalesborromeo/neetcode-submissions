class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_streak = 0
        max_streak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                consecutive_streak+=1
            else:
                consecutive_streak = 0
            max_streak = max(max_streak, consecutive_streak)

            
        return max_streak