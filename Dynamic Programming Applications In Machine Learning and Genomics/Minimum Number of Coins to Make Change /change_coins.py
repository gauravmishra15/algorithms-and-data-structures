#python3
import sys

def find_change(money, coins):
    # TODO: your code here
    return -1

if __name__ == "__main__":
    money = int(sys.stdin.readline().strip())
    coins = list(map(int, sys.stdin.readline().strip().split(',')))
    print(find_change(money, coins))

