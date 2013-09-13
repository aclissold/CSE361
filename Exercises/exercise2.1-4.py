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
# Output: A sequence of n or (n + 1) bits C = <c1, c2, ..., cn, cn+1> such
#   that C = A + B.
#
# BINARY-SUM(A, B)
# 1  carry = 0
# 2  Let C be a new array
# 3  for i = A.length downto 1
# 4      if (A[i] + B[i] + carry) == 3
# 5         carry = 1
# 6         C[i+1] = 1
# 7      elseif (A[i] + B[i] + carry) == 2
# 8         carry = 1
# 9         C[i+1] = 0
# 10     elseif (A[i] + B[i] + carry) == 1
# 11        carry = 0
# 12        C[i+1] = 1
# 13     else
# 14        carry = 0
# 15        C[i+1] = 0
# 16 if carry == 1
# 17     C[1] = 1
# 18 else
# 19     C[1] = 0
# 20 return C
#
# PYTHON:
def binary_sum(A, B):
    carry = 0
    C = []
    for i in reversed(xrange(len(A))):
        if (A[i] + B[i] + carry) == 3:
            carry = 1
            C.insert(0, 1)
        elif (A[i] + B[i] + carry) == 2:
            carry = 1
            C.insert(0, 0)
        elif (A[i] + B[i] + carry) == 1:
            carry = 0
            C.insert(0, 1)
        else:
            carry = 0
            C.insert(0, 0)
    if carry == 1:
        C.insert(0, 1)
    return C

if __name__ == '__main__':
    A = [1, 1, 0, 0, 1, 0, 0, 1]
    B = [1, 0, 0, 1, 1, 0, 1, 0]
    C = binary_sum(A, B)
    print C
