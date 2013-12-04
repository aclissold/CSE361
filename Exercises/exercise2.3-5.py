# Exercise 2.3-5
# -*- coding: utf-8 -*-
#
# DESCRIPTION:
# 
# Referring back to the searching problem (see Exercise 2.1-3), observe that if
# the sequence A is sorted, we can check the midpoint of the sequence against v
# and eliminate half of the sequence from further consideration. The binary
# search algorithm repeats this procedure, halving the size of the remaining
# portion of the sequence each time. Write pseudocode, either iterative or
# recursive, for binary search. Argue that the worst-case running time of binary
# search is Θ(lg n).
# 
# SOLUTION:
#
# PSEUDOCODE:
#
# LINEAR-SEARCH(A, v)
# 1 for i = 1 to A.length
# 2     if v == A[i]
# 3         return i
# 4 return NIL
def binary_search(A, v):
    if A[len(A)-1 / 2] == v:
        return len(A)/2

if __name__ == '__main__':
    A = [1, 13, 15, 18, 23, 34, 40, 44, 46, 47, 49, 50, 55, 63, 71, 78, 80, 95]
    v = 47
    print(binary_search(A, v))
