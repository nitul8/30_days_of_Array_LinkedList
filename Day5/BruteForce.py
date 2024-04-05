def profit(A):
    if len(A) <= 0:
        return 0
    A.sort()
    p = A[len(A)-1]-A[0]
    return p

A=[1,2,3,2,5,3]
print(profit(A))