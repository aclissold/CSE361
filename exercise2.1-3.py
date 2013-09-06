# Exercise 2.1-3
#
# DESCRIPTION:
#
# Consider the searching problem:
# 
# Input: A sequence of n numbers A = <a1, a2, ..., an> and a value v.
#
# Output: An index i such that v = A[i] or the special value NIL if v does not
#   appear in A.
#
# Write pseudocode for linear search, which scans through the sequence, looking
# for v. Using a loop invariant, prove that your algorithm is correct. Make
# sure that your loop invariant fulfills the three necessary properties.
#
# SOLUTION:
#
# LINEAR-SEARCH(A, v)
# 1 for i = 1 to A.length
# 2     if v == A[i]
# 3         return i
# 4 return NIL
#
# Loop invariant:
#   At the start of each iteration of the for loop of lines 1-3, an
#   i such that v = A[i] does not appear in the subarray A[1..j-1].
# Initialization: Before the first loop iteration, the subarray A[1..j-1]
#     is empty, and and i such that v = A[i] clearly cannot exist there, so
#     the loop invariant holds.
# Maintenance: Since the only way to terminate the loop is if v == A[i], the
#   loop invariant is preserved for the next iteration.
# Termination: When the loop terminates, it can only be because of one of two
#   cases: either an i was found such that v == A[i], meaning the value v was
#   found in the sequence A; or i > A.length, meaning the value was not found
#   in A. The output of the first case is the index i where v was found, and
#   the output of the second case is the special value NIL, so the algorithm is
#   correct.
#
# PYTHON:

def linear_search(A, v):
    for i in range(len(A)):
        if v == A[i]:
            return i
    # Python implicitly returns "None", basically
    # its NIL, even with no "return" statement

# TESTS:

A = [3, 5, 2, 6, 4, 3, 5, 7, 4]
print(linear_search(A, 5))
print(linear_search(A, 6))
print(linear_search(A, 0))
