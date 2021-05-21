class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #hashmap
        #math -> 2 * (a+b+c) - (a+a+b+b+c) = c
        #bitmasking -> a^0 = a and a^a = 0; a^b^a = a^a^b = 0^b = b
        a = 0
        for i in nums:
            a ^= i
        return a
