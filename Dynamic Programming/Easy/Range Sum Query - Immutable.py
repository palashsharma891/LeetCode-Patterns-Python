class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = [0] * (len(self.nums)+1)
        if len(nums):
            self.sum[0] = nums[0]
            for i in range(1, len(nums)):
                self.sum[i] = self.sum[i-1] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum[right]
        else:
            return self.sum[right] - self.sum[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
'''class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = 0#] * len(self.nums)
        
    def sumRange(self, left: int, right: int) -> int:
        self.sum = 0
        for i in range(left, right+1):
            self.sum += self.nums[i]
        return self.sum#[right] - self.sum[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)'''
