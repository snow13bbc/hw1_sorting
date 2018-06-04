import numpy as np
from example import algs
import random
import time
import matplotlib.pyplot as plt

def test_bubblesort():

    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    A = [1,2,4,0,1] #odd length
    B = [] #empty vector
    C = [2] #single element vector
    D = [23, 23, 42, 1, 32, 2] # Duplicated elements
    E = [1,2,4,0] #even length

    # test using exisiting sort function and also, just writing out what
    # the output should look like manually

    assert algs.bubblesort(A)[0] == sorted(A)
    assert algs.bubblesort(B)[0] == sorted(B)
    assert algs.bubblesort(C)[0] == sorted(C)
    assert algs.bubblesort(D)[0] == sorted(D)
    assert algs.bubblesort(E)[0] == [0,1,2,4]

    # algs.bubblesort(x)

def test_quicksort():

    A = [1,2,4,0,1] #odd length
    B = [] #empty vector
    C = [2] #single element vector
    D = [23, 23, 42, 1, 32, 2] # Duplicated elements
    E = [1,2,4,0] #even length

    # for now, just attempt to call the quicksort function, should
    # actually check output
    assert algs.quicksort(A,0,len(A)-1)[0] == sorted(A)
    assert algs.quicksort(B,0,len(B)-1)[0] == sorted(B)
    assert algs.quicksort(C,0,len(C)-1)[0] == sorted(C)
    assert algs.quicksort(D,0,len(D)-1)[0] == sorted(D)
    assert algs.quicksort(E,0,len(E)-1)[0] == [0,1,2,4] 

    # algs.quicksort(x,0,len(x)-1)
