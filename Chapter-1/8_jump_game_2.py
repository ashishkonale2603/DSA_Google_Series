def jump(nums):
    n=len(nums)
    count=0
    
    for i in range(n):
        store=0
        x=n
        for j in range(i,i+nums[i]):
            if x<=0:
                break
            else:
                x-=nums[j]
                store+=1
        
        if count<store:
            count=store

    return count

print(jump([2,3,1,1,4]))