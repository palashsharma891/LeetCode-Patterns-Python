class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        numlist = [nums[0]]
        for i in range(1, len(nums)):
            numlist += [nums[i] * numlist[i-1]]
            
        prod = 1
        print(numlist)
        
        for i in range(len(nums)-1, 0, -1):
            numlist[i] = numlist[i-1] * prod
            prod *= nums[i]
            
        numlist[0] = prod
        return numlist
