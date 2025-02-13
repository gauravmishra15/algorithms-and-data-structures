# Python3

import sys
from re import split
from random import choice


def deBruijn_graph_kmers(patterns):
    adj_list = {}
    for pattern in patterns:
        if pattern[:-1] not in adj_list:
            adj_list[pattern[:-1]] = [pattern[1:]]
        else:
            adj_list[pattern[:-1]].append(pattern[1:])
    return adj_list

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



def maximal_non_branching_paths(adj_list):
    paths = []

    # in and out degrees
    in_out_degrees = {}
    for source, targets in adj_list.items():
        if source not in in_out_degrees:
            in_out_degrees[source] = [0, len(targets)]
        else:
            in_out_degrees[source][1] += len(targets)

        for target in targets:
            if target not in in_out_degrees:
                in_out_degrees[target] = [1, 0]
            else:
                in_out_degrees[target][0] += 1

    # find all non-branching paths
    for v in list(in_out_degrees):
        if in_out_degrees[v] != [1, 1]:
            if in_out_degrees[v][1] > 0:
                while v in adj_list:
                    w = adj_list[v][0]
                    non_branching_path = [v, w]
                    adj_list = remove_edge(adj_list, v, w)
                    while in_out_degrees[w] == [1, 1]:
                        u = adj_list[w][0]
                        non_branching_path.append(u)
                        adj_list = remove_edge(adj_list, w, u)
                        w = u
                    paths.append(non_branching_path)

    # find isolated cycles
    while adj_list:
        start_node = list(adj_list)[0]
        current_node = adj_list[start_node][0]
        adj_list = remove_edge(adj_list, start_node, current_node)
        cycle = [start_node, current_node]
        while current_node != start_node:
            target_node = adj_list[current_node][0]
            cycle.append(target_node)
            adj_list = remove_edge(adj_list, current_node, target_node)
            current_node = target_node
        paths.append(cycle)

    return paths

def contig_generation(kmers):
    adj_list = deBruijn_graph_kmers(kmers)
    paths = maximal_non_branching_paths(adj_list)
    contigs = []
    for path in paths:
        contig = path[0]
        for edge in path[1:]:
            contig += edge[-1]
        contigs.append(contig)
    return contigs


if __name__ == "__main__":
    '''
    Given: A collection of k-mers Patterns.
    Return: All contigs in DeBruijn(Patterns). (You may return the strings in any order.)
    '''
    Patterns = sys.stdin.read().splitlines()
    contigs = contig_generation(Patterns)
    contigs.sort()
    print(" ".join(contigs))