class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx, val in enumerate(nums):
            need = target - val
            if need in mp:
                return [mp[need], idx]
            mp[val]=idx
             
