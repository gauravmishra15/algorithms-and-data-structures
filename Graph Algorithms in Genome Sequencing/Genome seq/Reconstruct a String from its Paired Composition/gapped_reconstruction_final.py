#python3

import sys
from collections import defaultdict
from re import split
from random import choice

def parse_adj_list(adj_list_text):
    adj_list = {}
    for elem in adj_list_text:
        temp = split(' -> ', elem)
        adj_list[temp[0]] = temp[1].split(',')
    return adj_list


def remove_edge(adj_list, from_node, to_node):
    adj_list[from_node].remove(to_node)
    if not adj_list[from_node]:
        del adj_list[from_node]
    return adj_list


def Eulerian_cycle(adj_list):
    # form a cycle Cycle by randomly walking in Graph
    start_node, edges = choice(list(adj_list.items()))
    target_node = choice(edges)
    adj_list = remove_edge(adj_list, start_node, target_node)

    Cycle = [start_node, target_node]
    current_node = target_node
    while current_node != start_node:
        edges = adj_list[current_node]
        target_node = choice(edges)
        adj_list = remove_edge(adj_list, current_node, target_node)
        current_node = target_node
        Cycle.append(current_node)

    while adj_list:
        potential_starts = [(idx, node) for idx, node in enumerate(Cycle) if node in adj_list]
        idx, new_start = choice(potential_starts)

        # form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
        new_cycle = Cycle[idx:] + Cycle[1:idx + 1]

        target_node = choice(adj_list[new_start])
        adj_list = remove_edge(adj_list, new_start, target_node)
        current_node = target_node
        new_cycle.append(current_node)
        while current_node != new_start:
            edges = adj_list[current_node]
            target_node = choice(edges)
            adj_list = remove_edge(adj_list, current_node, target_node)
            current_node = target_node
            new_cycle.append(current_node)
        Cycle = new_cycle
    return Cycle

def Eulerian_path(adj_list):
    deg_diffs = {}
    for source, targets in adj_list.items():
        if source in deg_diffs:
            deg_diffs[source] += len(targets)
        else:
            deg_diffs[source] = len(targets)
        for target in targets:
            if target in deg_diffs:
                deg_diffs[target] -= 1
            else:
                deg_diffs[target] = -1

    to_add_s = [node for node, diff in deg_diffs.items() if diff == -1][0]
    to_add_t = [node for node, diff in deg_diffs.items() if diff == 1][0]
    if to_add_s in adj_list:
        adj_list[to_add_s].append(to_add_t)
    else:
        adj_list[to_add_s] = [to_add_t]

    cycle = Eulerian_cycle(adj_list)
    idx = 0
    while True:
        if cycle[idx] == to_add_s and cycle[idx + 1] == to_add_t:
            break
        idx += 1
    return cycle[idx + 1:] + cycle[1:idx + 1]

def deBruijn_graph_paired_reads(paired_reads):
    adj_list = defaultdict(list)
    for pair in paired_reads:
        adj_list[(pair[0][:-1], pair[1][:-1])].append((pair[0][1:], pair[1][1:]))
    return adj_list


def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    prefix_string = ''
    suffix_string = ''
    for i, pattern_pair in enumerate(GappedPatterns):
        if i != len(GappedPatterns) - 1:
            prefix_string += pattern_pair[0][0]
            suffix_string += pattern_pair[1][0]
        else:
            prefix_string += pattern_pair[0]
            suffix_string += pattern_pair[1]
    for i in range(k + d + 1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d - 1]:
            return -1
    return prefix_string + suffix_string[len(suffix_string) - k - d - 1:]


def string_reconstruction_read_pairs(k, d, paired_reads):
    adj_list = deBruijn_graph_paired_reads(paired_reads)
    path = Eulerian_path(adj_list)
    return StringSpelledByGappedPatterns(path, k - 1, d)


if __name__ == "__main__":
    '''
    Given: Integers k and d followed by a collection of paired k-mers PairedReads.
    Return: A string Text with (k, d)-mer composition equal to PairedReads. (If multiple answers exist, you may return 
    any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    k, d = [int(x) for x in input_lines[0].split()]
    PairedReads = []
    for line in input_lines[1:]:
        PairedReads.append(line.split("|"))

    print(string_reconstruction_read_pairs(k, d, PairedReads))