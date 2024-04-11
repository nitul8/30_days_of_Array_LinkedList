
def repeatedNumber(self, A):
    temp = [0]*len(A)
    rept = -1
    miss = -1
    res = []
        
    for i in range(len(A)):
        temp[A[i]-1]+=1
        if(temp[A[i]-1]>1):
            rept = A[i]
            res.append(rept)
                
    for i in range(len(A)):
        if temp[i]==0:
            miss = i+1
            res.append(miss)
                
    return res