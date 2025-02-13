# Uses python3
import sys

def optimal_sequence_greedy(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence(value):
    best_num_ops = [value] * (value + 1)
    best_num_ops[0] = 0
    best_ops = [""] * (value + 1)

    for i in range(1, value + 1):
        # +1
        num_ops_1 = best_num_ops[i - 1] + 1

        # x2
        if i % 2 == 0:
            num_ops_2 = best_num_ops[i // 2] + 1
        else:
            num_ops_2 = value

        # x3
        if i % 3 == 0:
            num_ops_3 = best_num_ops[i // 3] + 1
        else:
            num_ops_3 = value

        num_ops = [num_ops_1, num_ops_2, num_ops_3]
        cur_best_num_ops = min(num_ops)
        cur_best_num_ops_idx = num_ops.index(cur_best_num_ops)

        best_num_ops[i] = cur_best_num_ops
        if cur_best_num_ops_idx == 0:
            best_ops[i] = "+1"
        elif cur_best_num_ops_idx == 1:
            best_ops[i] = "x2"
        elif cur_best_num_ops_idx == 2:
            best_ops[i] = "x3"
        else:
            raise

    values = []
    res = value
    while res != 0:
        values.append(res)
        if best_ops[res] == "+1":
            res -= 1
        elif best_ops[res] == "x2":
            res = res // 2
        elif best_ops[res] == "x3":
            res = res // 3
        else:
            raise

    values.reverse()

    return values


input = sys.stdin.read()
n = int(input)
#n = 10
results = optimal_sequence(n)
count = len(results) - 1
result = str(results)
print(count, result)