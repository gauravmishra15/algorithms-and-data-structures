#python3
import sys

class MinNumCoins:
    def __init__(self):
        self._input()
        print(self.DPChange(self.money, self.coins))
    
    def _input(self):
        data = sys.stdin.read().strip().split()
        self.money = int(data[0])
        self.coins = [int(c) for c in data[1].split(',')]

    def DPChange(self, money, coins):
        minNumCoins = [0]
        for m in range(1, money + 1):
            globalMin = float('inf')
            for coin in coins:
                if m >= coin:
                    currMin = minNumCoins[m-coin] + 1
                    if currMin < globalMin:
                        globalMin = currMin
            minNumCoins.append(globalMin)
        return minNumCoins[money]                       

if __name__ == "__main__":
    MinNumCoins()