def maxMod(A):
    a = -999 #largest value of array
    b = -999 #second largest value of array
    
    n = len(A)
    for i in range(n):
        if a < A[i]:
            b = a
            a = A[i]
        elif b<A[i] and a!=A[i]:
            b = A[i]
    return 0 if b < 0 else b