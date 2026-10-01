class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        input: int array nums and val

        we need to: 
            -remove all occurrences of val in nums in place.
            -change the array nums such that the first k elements of nums 
            contain the elements which are not equal to val.
            -the remaining elements of nums are not important as well as the
            size of nums

        output: int k
        '''
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k