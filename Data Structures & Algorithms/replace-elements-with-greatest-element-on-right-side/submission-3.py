class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        for i in range(len(arr)-1, -1, -1):
            current_val = arr[i]
            arr[i] = max_right
            max_right = max(current_val, max_right)
        return arr