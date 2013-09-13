# Exercise 2.2-2
#
# DESCRIPTION:
#
# Consider sorting n numbers stored in array A by first finding the smallest
# element on A and exchanging it with the element n A[1]. Then find the second
# smallest element of A, and exchange it with A[2]. Continue in this manner
# for the first n - 1 elements on A. Write pseudocode for this algorithm, which
# is known as selection sort. What loop invariant does this algorithm maintain?
# Why does it need to run for only the first n - 1 elements, rather than for
# all n elements? Give the best-case and worst-case running times of selection
# sort in Θ-notation.
#
# SOLUTION:
#
# SELECTION-SORT(A)
# 1 for j = 1 to A.length - 1
# 2     key = A[j]
# 3     loc = j
# 4     for i = j + 1 to A.length
# 5         if A[i] < key
# 6             key = A[i]
# 7             loc = i
# 8     A[loc] = A[j]
# 9     A[j] = key
#
# Loop invariant: At the start of each iteration of the for loop of lines 1-9,
# the subarray A[1..j-1] consists of elements originally in A[1..j-1], but in
# sorted order. Note that this is the same loop invariant as for
# INSERTION-SORT.
#
# This algorithm doesn't need to execute the would-be nth step because the nth
# element is the greater than or equal to all other elements in the array
# (otherwise it would have been found by line 5 prior to this point and sorted
# into the subarray).
#
# Best-case AND worst-case running time: Θ(n^2), because every element in the
# array must be iterated over, whether or not it is already in a sorted or
# semi-sorted order.
#
# PYTHON:
def selection_sort(A):
    for j in xrange(0, len(A) - 1):
        key = A[j]
        loc = j
        for i in xrange(j + 1, len(A)):
            if A[i] < key:
                key = A[i]
                loc = i
        A[loc] = A[j]
        A[j] = key

if __name__ == '__main__':
    A = [6, 5, 2, 4, 7, 1, 3, 9, 8]
    selection_sort(A)
    print A
