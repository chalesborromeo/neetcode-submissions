class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for index, value in enumerate(nums):
            ind_val = target - value
            if ind_val in output:
                return[output[ind_val], index]
            output[value] = index