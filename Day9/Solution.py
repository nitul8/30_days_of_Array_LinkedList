def trap(A):
    ans = 0
    n = len(A)
    
    left = [0] * n
    right = [0] * n
    lefty = float('-inf')
    righty = float('-inf')
    
    for i in range(n):
        left[i] = max(lefty, A[i])
        lefty = left[i]
        right[n-i-1] = max(righty, A[n-i-1])
        righty = right[n-i-1]
    
    for i in range(n):
        ans += min(left[i], right[i]) - A[i]
    
    return ans