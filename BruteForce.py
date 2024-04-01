def maxMod(A):
    big = 0
    n = len(A)
    for i in range(n-1):
        for j in range(i+1,n-1):
            mod = A[i]%A[j]
            if mod > big:
                big = mod
    return big

A=[1,2,3,4,5,6]
print("Max mod is : ",maxMod(A))