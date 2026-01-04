class Solution(object):
    def jump(self,nums):

        n=len(nums)
        m=0

        for i in range(n):
            if i>m:
                return False
            
            m=max(m,i+nums[i])
        return True
    
s=Solution()
nums = [3,2,1,0,4]
print(s.jump(nums))
