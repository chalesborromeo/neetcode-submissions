class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        you need to convert all of the letters of the alphabet, then use those 
        values to compare them to the other anagrams inside of the array to 
        make the subarray.
        '''
        subarray_dict = defaultdict(list)

        for s in strs:
            char = [0] * 26
            for c in s:
                char[ord(c)-ord('s')]+=1

            subarray_dict[tuple(char)].append(s)
        return list(subarray_dict.values())