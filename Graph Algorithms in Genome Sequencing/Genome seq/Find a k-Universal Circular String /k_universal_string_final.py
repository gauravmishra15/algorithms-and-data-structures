#python3

import sys
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

def deBruijn_graph_kmers(patterns):
    adj_list = {}
    for pattern in patterns:
        if pattern[:-1] not in adj_list:
            adj_list[pattern[:-1]] = [pattern[1:]]
        else:
            adj_list[pattern[:-1]].append(pattern[1:])
    return adj_list

def k_universal_circular_string(k):
    kmers = []
    for i in range(2 ** k):
        kmer = str(bin(i))[2:]
        if len(kmer) != k:
            kmer = '0' * (k - len(kmer)) + kmer
        kmers.append(kmer)

    adj_list = deBruijn_graph_kmers(kmers)
    cycle = Eulerian_cycle(adj_list)

    cycle = cycle[:len(cycle) - k + 1]
    string = cycle[0][:-1]
    for r in cycle:
        string += r[-1]
    return string


if __name__ == "__main__":
    '''
    Given: An integer k.
    Return: A k-universal circular string. (If multiple answers exist, you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])

    print(k_universal_circular_string(k))