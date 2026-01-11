class Solution(object):
    def rotate(self,mat,target):

        n=len(mat)

        bool=False
        if mat==target:
            bool=True
        for k in range(4):
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(n):
                mat[i].reverse()
            if mat==target:
                bool=True
        return bool
    
sol = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
print(sol.rotate(mat,target))