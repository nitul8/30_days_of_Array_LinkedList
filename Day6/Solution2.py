#Second optimal solution

def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        
        row = [1] * (rowIndex + 1)
        
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                row[i - j] += row[i - j - 1]
                
        return row