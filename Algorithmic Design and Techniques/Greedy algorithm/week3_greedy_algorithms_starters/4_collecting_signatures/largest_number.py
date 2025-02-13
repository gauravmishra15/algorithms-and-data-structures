# Uses python3

import sys

def largest_number(a):
    # write your code here
    number = a.sort()

    res = ""
    #for x in a:
    for x in number:
        res += x
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))