class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        for i in range(numRows - 1):
            row = [1] * (len(res[-1]) + 1)
            for j in range(1, len(row) - 1):
                row[j] = res[-1][j] + res[-1][j - 1]
            res.append(row)
        
        return res
                
        
                
                