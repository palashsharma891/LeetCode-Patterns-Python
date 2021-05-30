class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # basic soln -> hash table -> won't work coz' map can't be formed!
        '''
        num_dict = {}
        for num in range(1, len(nums)+1):
            if num in nums:
                if num in num_dict:
                    num_dict[num] += 1
                else:
                    num_dict[num] = 1
        print(num_dict)
        arr = []
        for num in num_dict:
            if num_dict[num] == 0:
                arr += [num]
                
        return arr'''
        ''' 
        # tc O(n) sc O(n)
        all_numbers_set = set(range(1, len(nums)+1))
        for num in nums:
            if num in all_numbers_set:
                all_numbers_set.remove(num)
        return list(all_numbers_set)
        '''
        # tc O(n) sc O(1)
        missing = []
        for num in nums:
            pos = abs(num)-1
            if nums[pos] > 0:
                nums[pos] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                missing += [i+1]
                
        return missing
