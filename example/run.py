# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort
import random
import time
import matplotlib.pyplot as plt

def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    A = np.random.rand(10)
    print("Unsorted input: ", A)

    print("Bubble sort output: ", bubblesort(A))
    print("Quick sort output: ", quicksort(A,0,len(A)-1,0,0))

    #Checking Time Complexity
    QuicksortTimes = []
    bubbleSortTimes = []

    sizes = [100*x for x in range (0,11)]
    for i in sizes:
        randomList = np.random.random_integers(1,1000000000,size=i)

        startTime = time.time()
        quickList = quicksort(randomList,0,len(randomList)-1,0,0)
        runTime = time.time()-startTime
        QuicksortTimes.append(runTime)

        startTime = time.time()
        quickList = bubblesort(randomList)
        runTime = time.time()-startTime
        bubbleSortTimes.append(runTime)

    plt.figure(figsize=(12,5))
    plt.plot(sizes,QuicksortTimes,marker='x',c='b',label='Quicksort')
    plt.plot(sizes,bubbleSortTimes,marker='x',c='r',label='Bubblesort')
    plt.xlabel("size of unsorted list")
    plt.ylabel("seconds of computation")
    plt.legend(loc=2)
    plt.grid()
    plt.title("Quicksort vs Bubblesort")

    plt.show()
