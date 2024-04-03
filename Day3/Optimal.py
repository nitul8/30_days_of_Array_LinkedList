#optimal solution
def count_even_vs_odd(A):
    even = odd = 0
    for num in A:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return min(even, odd)