class Solution(object):
    def rotate(self,matrix):
        n=len(matrix)
        print(n)
        
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol=Solution()
print(sol.rotate(matrix))