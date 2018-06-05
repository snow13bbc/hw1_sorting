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

    print("Bubblesort output, number of assignments, number of conditionals: ", bubblesort(A))
    print("Quicksort output, number of assignments, number of conditionals: ", quicksort(A,0,len(A)-1))

    #Checking Time Complexity
    arr_val = []
    bs_assigns, bs_conds = [], []
    qs_assigns, qs_conds = [], []

    for i in range(0, 1000, 100):
        arr_val.append(i)
        iter_bs_assigns, iter_bs_conds = [], []
        iter_qs_assigns, iter_qs_conds = [], []

        for j in range(0, 10):
            x = np.random.rand(i)

            b_sort = bubblesort(x)
            iter_bs_assigns.append(b_sort[1])
            iter_bs_conds.append(b_sort[2])

            q_sort = quicksort(x, 0, len(x) - 1)
            iter_qs_assigns.append(q_sort[1])
            iter_qs_conds.append(q_sort[2])

        bs_assigns.append(np.average(iter_bs_assigns))
        bs_conds.append(np.average(iter_bs_conds))
        qs_assigns.append(np.average(iter_qs_assigns))
        qs_conds.append(np.average(iter_qs_conds))

    print("N^2", [i**2 for i in range(0, 1000, 100)])
    print("bubble assignments" , bs_assigns)
    print("NlogN", [i * np.log(i) for i in range(0, 1000, 100)])
    print("quicksort assignments", qs_assigns)
    plt.xlabel("list length")
    plt.ylabel("# of assignments")
    plt.plot(arr_val, [i**2 for i in range(0, 1000, 100)], label = "N^2")
    plt.plot(arr_val, bs_assigns, label = "bubblesort")
    plt.plot(arr_val, [15 *i * np.log(i) for i in range(0, 1000, 100)], label = "Nln(N)")
    plt.plot(arr_val, qs_assigns, label = "quicksort")
    plt.legend()
    plt.savefig("assignments.png")
    plt.show()


    print("bubble conditionals", bs_conds)
    print("quicksort conditionals", qs_conds)
    plt.xlabel("list length")
    plt.ylabel("# of conditionals")
    plt.plot(arr_val, [i**2 for i in range(0, 1000, 100)], label = "N^2")
    plt.plot(arr_val, bs_conds, label = "bubblesort")
    plt.plot(arr_val, [15 * i * np.log(i) for i in range(0, 1000, 100)], label = "Nln(N)")
    plt.plot(arr_val, qs_conds, label = "quicksort")
    plt.legend()
    plt.savefig("conditionals.png")
    plt.show()
