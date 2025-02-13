# Uses python3
import sys

def get_majority_element(a, left, right):
    # create an empty `HashMap`
    dict = {}

    # store each element's frequency in a dictionary
    for i in A:
        dict[i] = dict.get(i, 0) + 1

    # return the element if its count is more than `n/2`
    for key, value in dict.items():
        if value > len(A) / 2:
            return key

    # no majority element is present
    return -1

    return -1

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    a = [2, 3, 9, 2, 2]
    n = 5
    if get_majority_element(a, 0, n) != -1:
        print(get_majority_element(a, 0, n))
    else:
        print(0)
