# Exercise 2.1-4
#
# DESCRIPTION:
#
# Consider the problem of adding two n-bit binary integers, stored in two
# n-element arrays A and B. The sum of the two integers should be stored n
# binary form in an (n + 1)-element array C. State the problem formally and
# write pseudocode for adding the two integers.
# 
# SOLUTION:
#
# Input: Two sequences of n bits A = <a1, a2, ..., an> and
#   B = <b1, b2, ..., bn>.
# Output: A sequence of n + 1 bits C = <c1, c2, ..., cn, cn+1> such that C =
#   A + B.
#
# BINARY-SUM(A, B)
# 1 for i = A.length downto 1
# 2     if A[i] == 0 and B[i] == 0
# 3         C[i] = 0
# 4     elseif A[i] == 1 and B[i] == 1
# 5         C[i] = 0
# 6         carry = 1
# 7     else
# 8         C[i] = 1
