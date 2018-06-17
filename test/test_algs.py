import numpy as np
from Sorting_Functions import algs
import random
import time
import matplotlib.pyplot as plt

def test_bubblesort_odd():
    A = [1,2,4,0,1] #odd length
    assert algs.bubblesort(A)[0] == sorted(A)

def test_bubblesort_empty():
    B = [] #empty vector
    assert algs.bubblesort(B)[0] == sorted(B)

def test_bubblesort_single():
    C = [2] #single element vector
    assert algs.bubblesort(C)[0] == sorted(C)

def test_bubblesort_duplicate():
    D = [23, 23, 42, 1, 32, 2] # Duplicated elements
    assert algs.bubblesort(D)[0] == sorted(D)

def test_bubblesort_even():
    E = [1,2,4,0] #even length
    assert algs.bubblesort(E)[0] == sorted(E)

def test_quicksort_odd():
    A = [1,2,4,0,1] #odd length
    assert algs.quicksort(A,0,len(A)-1)[0] == sorted(A)

def test_quicksort_empty():
    B = [] #empty vector
    assert algs.quicksort(B,0,len(B)-1)[0] == sorted(B)

def test_quicksort_odd():
    C = [2] #single element vector
    assert algs.quicksort(C,0,len(C)-1)[0] == sorted(C)

def test_quicksort_duplicated():
    D = [23, 23, 42, 1, 32, 2] # Duplicated elements
    assert algs.quicksort(D,0,len(D)-1)[0] == sorted(D)

def test_quicksort_even():
    E = [1,2,4,0] #even length
    assert algs.quicksort(E,0,len(E)-1)[0] == sorted(E)
