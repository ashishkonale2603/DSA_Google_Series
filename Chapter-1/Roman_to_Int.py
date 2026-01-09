class Solution(object):
    def romanToInt(self,s):
        #store the values in hash
        store= {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        total=0

        for i in range(len(s)-1):
            if store[s[i]] < store[s[i + 1]]:
                total -= store[s[i]]
            else:
                total += store[s[i]]
        return total + store[s[-1]]