class Solution:
    
    def countBits(self, n):
        dp = [0] * (n+1)
        for i in range(n+1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i // 2] + 1
        return dp
    '''
    def convert_to_binary(self, num):
        s = ''
        while num >= 1:
            s += str(num % 2)
            num //= 2
        return s[::-1]
    
    def countBits(self, n: int) -> List[int]:
        binary_list = []
        for i in range(n+1):
            binary = self.convert_to_binary(i)
            binary_list += [binary.count('1')]
        return binary_list
    '''
