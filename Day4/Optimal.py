def odd_even_sequence(A):
    conut = 0
    for i in range(len(A)-1):
        curr = A[i]
        next = A[i+1]
        
        if curr%2 == 0 and next%2 == 1:
            count+=1
        elif curr%2 == 1 and next%2 == 0:
            count+=1
    return count