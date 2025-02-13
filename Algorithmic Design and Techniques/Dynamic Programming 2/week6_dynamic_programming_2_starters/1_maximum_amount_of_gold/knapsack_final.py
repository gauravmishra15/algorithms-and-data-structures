# Uses python3
import sys

def optimal_weight(W, w):
    golds = [0] + w
    gold_dict = {}
    for i in range(0, W+1):
        gold_dict[(i, 0)] = 0
    for i in range(0, len(golds)):
        gold_dict[(0, i)] = 0
    for i in range(1, len(golds)):
        for weight in range(1, W+1):
            gold_dict[(weight, i)] = gold_dict[(weight, (i-1))]
            if golds[i] <= weight:
                val = gold_dict[(weight-golds[i], i-1)] + golds[i]
                if gold_dict[(weight, i)] < val:
                    gold_dict[(weight, i)] = val
    return max(gold_dict.values())

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
