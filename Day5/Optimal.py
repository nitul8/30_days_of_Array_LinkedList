def profit(A):
    if len(A) <= 0:
        return 0
    minimum = A[0]
    op = 0
    for i in range(len(A)):
        minimum = min(A[i],minimum)
        op = max(op,A[i]-minimum)
        
    return op