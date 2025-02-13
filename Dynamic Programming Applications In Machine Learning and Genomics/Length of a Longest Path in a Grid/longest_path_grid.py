#python3
import sys

def longest_path(n,m,down,right):
    # TODO: your code here
    return -1

if __name__ == "__main__":
    n,m = map(int, sys.stdin.readline().strip().split())
    down = [list(map(int, sys.stdin.readline().strip().split()))
            for _ in range(n)]
    sys.stdin.readline()
    right = [list(map(int, sys.stdin.readline().strip().split()))
            for _ in range(n+1)]

    print(longest_path(n,m,down,right))
