class trapping_water(object):
    def trapWater(self, height):
        l=0
        r=len(height)-1
        lMax=height[l]
        rMax=height[r]
        result=0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                result+=lMax-height[l]

            else:
                r-=1
                rMax = max(rMax, height[r])
                result+=rMax-height[r]
        return result
    
height=[0,1,0,2,1,0,1,3,2,1,2,1]
tw= trapping_water()
print(tw.trapWater(height))