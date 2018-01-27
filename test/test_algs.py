import numpy as np
from example import algs
import random
import time
import matplotlib.pyplot as plt

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

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

    # for now, just attempt to call the bubblesort function, should
    # actually check output
    assert algs.bubblesort(A) == sorted(A)
    assert algs.bubblesort(B) == sorted(B)
    assert algs.bubblesort(C) == sorted(C)
    assert algs.bubblesort(D) == sorted(D)
    assert algs.bubblesort(E) == sorted(E)

    # algs.bubblesort(x)

def test_quicksort():

    A = [1,2,4,0,1] #odd length
    B = [] #empty vector
    C = [2] #single element vector
    D = [23, 23, 42, 1, 32, 2] # Duplicated elements
    E = [1,2,4,0] #even length

    # for now, just attempt to call the quicksort function, should
    # actually check output
    assert algs.quicksort(A,0,len(A)-1,0,0) == sorted(A)
    assert algs.quicksort(B,0,len(B)-1,0,0) == sorted(B)
    assert algs.quicksort(C,0,len(C)-1,0,0) == sorted(C)
    assert algs.quicksort(D,0,len(D)-1,0,0) == sorted(D)
    assert algs.quicksort(E,0,len(E)-1,0,0) == sorted(E)

    # algs.quicksort(x,0,len(x)-1)
