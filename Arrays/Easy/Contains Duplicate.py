class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return not len(set(nums)) == len(nums)
        dic = {}
        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = 1
        return False

# 2nd attempt
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
