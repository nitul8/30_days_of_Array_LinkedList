#To sort the Array A using bubble sort

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A

#To find the strictly increasing and decreasing vlue in the array
def SaG(A):
    bubbleSort(A)
    n = len(A)
    
    count=0
    for i in range(n-1):
        if A[i]-1 == A[i-1] and A[i]+1  == A[i+1]:
            count +=1
            
    return count