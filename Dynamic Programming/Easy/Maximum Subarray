class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -100001
        temp_sum = 0
        for i in range(len(nums)):
            temp_sum += nums[i]
            if temp_sum >= max_sum:
                max_sum = temp_sum
            if temp_sum < 0: #if -ve, start from next num cuz if we continue adding, there is no use bruh....
                temp_sum = 0
        return max_sum
