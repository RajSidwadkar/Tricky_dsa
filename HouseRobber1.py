def rob(nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1] #dp[-1]

print(rob([2,7,9,3,1]))

#Solution 2

def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        temp = prev = 0
        
        current = 0

        for i in range(n):
            current = max(prev, temp + nums[i])
            temp = prev
            prev = current


        return current
