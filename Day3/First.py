#First approach
def count_even_odd(A):
    even = odd = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if even < odd: 
        return even 
    else: 
        return odd