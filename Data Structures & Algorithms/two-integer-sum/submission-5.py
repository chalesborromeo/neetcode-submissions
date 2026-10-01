class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in output:
                return [output[diff], index ]
            output[value] = index