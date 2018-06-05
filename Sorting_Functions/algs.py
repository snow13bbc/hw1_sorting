import numpy as np
import sys
sys.setrecursionlimit(10000)

def bubblesort(A):
    n_assign = 0 #number of assignments
    n_cond = 0 #number of conditions
    n = len(A)

    if n == 0:
        return A, n_assign, n_cond

    for i in range(n):
        n_assign += 1
        for j in range(0, n-i-1):
            n_assign += 1
            if A[j] > A[j+1] :
                n_cond += 1
                A[j], A[j+1] = A[j+1], A[j]
                n_assign +=1
            else:
                n_cond += 1
    return A, n_assign, n_cond

qs_assign, qs_cond = 0, 0
def quicksort(A,p,r):
    global qs_assign, qs_cond

    if len(A) in (0,1):
        qs_cond += 1
        return A,qs_assign, qs_cond

    def partition(arr,first,last):
        global qs_assign, qs_cond

        x = arr[last] # choosing the pivot as the last element in the array
        i = first - 1 #start index
        for j in range(first,last):
            if A[j] <= x:
                qs_cond += 1
                i = i+1
                qs_assign += 1
                arr[i],arr[j] = arr[j],arr[i]
                qs_assign += 2
        arr[i+1],arr[last]=arr[last],arr[i+1]
        qs_assign += 2
        return i+1

    if p < r:
        qs_cond += 1
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        qs_assign += 1
        quicksort(A,q+1,r)
        qs_assign += 1
        return A, qs_assign, qs_cond
