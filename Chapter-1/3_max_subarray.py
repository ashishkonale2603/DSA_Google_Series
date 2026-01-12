class Solution(object):
    def maxSubArray(self, nums):
        
        maxSub=nums[0]
        curSum=0
        for n in nums:
            if curSum <0:
                curSum=0
            curSum+=n
            maxSub=max(maxSub,curSum)
        return maxSub
        
sol=Solution()
nums=[5,4,-1,7,8]
print(sol.maxSubArray(nums))