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
    n_assign = 0 #number of assignments
    n_cond = 0 #number of conditions
    n = len(A)
    for i in range(n):
        n_assign += 1
        for j in range(0, n-i-1):
            if A[j] > A[j+1] :
                n_cond += 1
                A[j], A[j+1] = A[j+1], A[j]
                n_assign +=1
    return A, n_assign, n_cond

def Partition (A,p,r,n_assign,n_cond):
    n_assign = 0 #number of assignments
    n_cond = 0 #number of conditions
    x = A[r] # choosing the pivot as the last element in the array
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            n_cond += 1
            i = i+1
            n_assign += 1
            A[i],A[j] = A[j],A[i]
            n_assign += 1
    A[i+1],A[r]=A[r],A[i+1]
    n_assign += 1
    return i+1

def quicksort(A,p,r,n_assign,n_cond):
    n_assign = 0 #number of assignments
    n_cond = 0 #number of conditions

    if len(A)==0:
        n_cond += 1
        return [],n_assign,n_cond
    if len(A)==1:
        n_cond += 1
        return A,n_assign,n_cond
    if p < r:
        n_cond += 1
        q = Partition(A,p,r,n_assign,n_cond)
        quicksort(A,p,q-1, n_assign,n_cond)
        n_assign += 1
        quicksort(A,q+1,r,n_assign,n_cond)
        n_assign += 1
        return A, n_assign, n_cond
