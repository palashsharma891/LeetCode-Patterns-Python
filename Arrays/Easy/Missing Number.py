class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
                
        for num in range(len(nums)+1):
            if num not in num_dict:
                return num
        #hash_map approach, works fine                
        '''
        #bit manipulation
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i^nums[i]
        return missing
