class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        pseudocode:

        perform (one at a time):
        1. subarray -> nums[i..j], the condition is 0<=i<=j<=n-1
        2. use int x and add it to all of the elements in the nums subarray

        goal:
        find the max frequncy of the value k after operation
        """
        # kadane's algorithm???

        # initialize countK 
        countK = nums.count(k)
        result = 0

        for i in range(1, 51):
            if i == k:
                continue
            count = 0
            for num in nums:
                if num == i:
                    count += 1
                if num == k:
                    count -= 1
                count = max(count, 0)
                result = max(result, countK + count)
        return result

