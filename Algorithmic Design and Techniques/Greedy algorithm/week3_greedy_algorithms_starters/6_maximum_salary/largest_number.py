# Uses python3

import sys
from itertools import permutations


def largest_number(a):
    extval, ans = [], ""
    l = len(str(max(a))) + 1
    for i in a:
        temp = str(i) * l
        extval.append((temp[:l:], i))

    extval.sort(reverse=True)
    for i in extval:
        ans += str(i[1])

    if int(ans) == 0:
        return "0"
    return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))