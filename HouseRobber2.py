def rob(nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        withoutstart = robber(nums[1:])
        withoutend = robber(nums[:-1])
        return max(withoutstart, withoutend)
    
def robber(houses):
    prevrob = maxrob = 0

    for money in houses:
        temp = max(maxrob, prevrob + money)
        prevrob = maxrob
        maxrob = temp

    return temp

print(rob([2,7,9,3,1]))
