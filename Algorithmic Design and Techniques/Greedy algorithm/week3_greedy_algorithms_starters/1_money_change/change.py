# Uses python3

import sys

def get_change(m):
    ## number of coins for the greatest currency coin first
    n = 0;

    if m > 10:
        x = m % 10
        x10 = m//10
        x5 = x//5
        x1 = x % 5
        n = x10 + x5 + x1
        return n

    ## number of coins for the second greatest currency coin secnd

    if m < 10 & m > 5:
        x5 = m // 5
        x1 = m % 5
        n = x5 + x1
        return n

    if m < 5:
        return m

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = 11
    print(get_change(m))
