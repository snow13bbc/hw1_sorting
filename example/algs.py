import numpy as np
import sys
sys.setrecursionlimit(10000)

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
    return A

def Partition (A,p,r):
    x = A[r] # choosing the pivot as the last element in the array
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quicksort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
        return A
