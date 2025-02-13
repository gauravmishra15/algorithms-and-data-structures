# Uses python3
import sys
from collections import namedtuple

Item = namedtuple("Item", "value weight")


def get_optimal_value(capacity, weights, values):
    # write your code here

    weight_value_pairs = sorted(
        [Item(v, w) for v, w in zip(values, weights)],
        key=lambda i: i.value / i.weight,
        reverse=True
    )

    totalValue = 0
    spaceleft = int(capacity)

    for item in weight_value_pairs:
        if spaceleft == 0:
            return (totalValue)

        a = min(item.weight, spaceleft)
        totalValue = totalValue + a * (item.value / item.weight)
        spaceleft = spaceleft - a
    return (totalValue)
    # return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))