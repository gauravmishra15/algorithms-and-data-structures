# python3
import sys


def SortCharacters(s):
    order = [0] * len(s)
    count = {'$': 0, "A": 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        count[char] += 1
    ele = ['$', 'A', 'C', 'G', 'T']
    for i in range(1, 5):
        count[ele[i]] += count[ele[i-1]]
    for j in range(len(s) - 1, -1, -1):
        c = s[j]
        count[c] -= 1
        order[count[c]] = j
    return order


def ComputeCharClasses(s, order):
    char_class = [0] * len(s)
    for i in range(1, len(s)):
        if s[order[i]] == s[order[i-1]]:
            char_class[order[i]] = char_class[order[i-1]]
        else:
            char_class[order[i]] = char_class[order[i-1]] + 1
    return char_class


def SortDoubled(s, L, old_order, old_class):
    count = [0] * len(s)
    new_order = [0] * len(s)
    for i in range(len(s)):
        count[old_class[i]] += 1
    for i in range(1, len(s)):
        count[i] += count[i-1]
    for j in range(len(s) - 1, -1, -1):
        start = (old_order[j] - L + len(s)) % len(s)
        cl = old_class[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def UpdateClasses(new_order, old_class, L):
    n = len(new_order)
    new_class = [0] * n
    for i in range(1, n):
        cur = new_order[i]
        mid = (cur + L) % n
        prev = new_order[i-1]
        mid_prev = (prev + L) % n
        if old_class[cur] == old_class[prev] and old_class[mid] == old_class[mid_prev]:
            new_class[cur] = new_class[prev]
        else:
            new_class[cur] = new_class[prev] + 1
    return new_class


def BuildSuffixArray(s):
    order = SortCharacters(s)
    _class = ComputeCharClasses(s, order)
    L = 1
    while L < len(s):
        order = SortDoubled(s, L, order, _class)
        _class = UpdateClasses(order, _class, L)
        L = 2 * L
    return order[1:]


def PatternMatchingWithSuffixArray(t, p, sa):
    # print(sa)
    min = 0
    max = len(t)
    while min < max:
        mid = (min + max) // 2
        # print(min, max, mid)
        suffix = sa[mid]
        i = 0
        while i < len(p) and suffix + i < len(t):
            if p[i] > t[suffix + i]:
                min = mid + 1
                break
            elif p[i] < t[suffix + i]:
                max = mid
                break
            i += 1
            if i == len(p):
                max = mid
            elif suffix + i == len(t):
                min = mid + 1
    start = min
    # print(start)
    max = len(t)
    while min < max:
        mid = (min + max) // 2
        # print(min, max, mid)
        suffix = sa[mid]
        i = 0
        while i < len(p) and suffix + i < len(t):
            if p[i] < t[suffix + i]:
                max = mid
                break
            i += 1
            if i == len(p) and i <= len(t) - suffix:  # if p is a prefix of the suffix, we treat p >= suffix
                min = mid + 1
    end = max - 1
    return start, end


if __name__ == '__main__':
    text = input()
    n_patterns = int(input())
    patterns = list(input().split())
    suffix_array = BuildSuffixArray(text+'$')
    result = [0] * len(text)
    for pattern in patterns:
        s, e = PatternMatchingWithSuffixArray(text, pattern, suffix_array)
        if s <= e:
            for i in range(s, e + 1):
                pos = suffix_array[i]
                if result[pos] == 0:
                    print(pos, end=' ')
                result[pos] += 1