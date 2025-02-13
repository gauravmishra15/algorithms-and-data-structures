# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # initialize empty `HashMap`
    dict = {}
    majority_count = 0

    # store each element's frequency in a dictionary
    for i in a:
        dict[i] = dict.get(i, 0) + 1

    # return the element if its count is more than `n/2`
    for key, value in dict.items():
        if value > len(a) / 2:
            #return key
            majority_count += 1
    return majority_count

    # no majority element is present
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #a = [4, 4, 5, 5, 5, 4, 5, 5, 5, 4, 4, 4, 5, 5, 4, 5, 5, 4, 5, 4, 4, 5, 5, 4, 5, 5, 4, 4 , 4, 4, 5, 5]
    #n = 5
    if get_majority_element(a, 0, n) != -1:
        print(get_majority_element(a, 0, n))
    else:
        print(0)
