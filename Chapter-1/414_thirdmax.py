class Solution():
    def thirdmax(self,nums):
        
        out=[]
        for  i in nums:
            if i not in out:
                out.append(i)
        sortList=sorted(out)

        if len(sortList)>=3:
            return sortList[-3]
        else:
            return sortList[-1]

lst=[2,2,3,1]
s=Solution()
print(s.thirdmax(lst))
