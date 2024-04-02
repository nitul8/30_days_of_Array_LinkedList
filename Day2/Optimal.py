def SaG(A):
    A.sort()
    n = len(A)
    count=0
    
    for i in range(1,n-1):
        if A[i]>A[0] and A[i]<A[n-1]:
            count +=1
            
    return count