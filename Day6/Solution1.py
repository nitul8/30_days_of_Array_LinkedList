#This solution is the one of it's solutions

def getRow(self, A):
        ans = []
        p = 1
        ans.append(1)
        
        for i in range(1, A):
            c = (p * (A - i + 1)) // i
            ans.append(c)
            p = c
        
        if A > 0:
            ans.append(1)
        
        return ans