# Uses python3
import sys
import itertools


# Helper function for solving 3 partition problem.
# It returns true if there exist three subsets with the given sum
def subsetSum(S, n, a, b, c):
    # return true if the subset is found
    if a == 0 and b == 0 and c == 0:
        return True

    # base case: no items left
    if n < 0:
        return False

    # Case 1. The current item becomes part of the first subset
    A = False
    if a - S[n] >= 0:
        A = subsetSum(S, n - 1, a - S[n], b, c)

    # Case 2. The current item becomes part of the second subset
    B = False
    if not A and (b - S[n] >= 0):
        B = subsetSum(S, n - 1, a, b - S[n], c)

    # Case 3. The current item becomes part of the third subset
    C = False
    if (not A and not B) and (c - S[n] >= 0):
        C = subsetSum(S, n - 1, a, b, c - S[n])

    # return true if we get the solution
    return A or B or C


# Function for solving the 3–partition problem. It returns true if the given
# set `S[0…n-1]` can be divided into three subsets with an equal sum.
def partition(S):
    if len(S) < 3:
        return False

    # return true if the sum is divisible by 3 and the set `S` can
    # be divided into three subsets with an equal sum
    return (sum(S) % 3) == 0 and \
           subsetSum(S, len(S) - 1, sum(S) / 3, sum(S) / 3, sum(S) / 3)


def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

