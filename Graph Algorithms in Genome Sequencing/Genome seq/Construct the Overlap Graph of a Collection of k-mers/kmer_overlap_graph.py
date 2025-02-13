#python3
import sys


def overlap_graph(patterns):
    """Creates an overlap graph from a list of k-mers

    Args:
        patterns:       a list of string k-mers

    Returns:
        a string containing an adjacency list representation of the overlap
        graph as described in the problem specification
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    patterns = sys.stdin.read().strip().splitlines()
    print(overlap_graph(patterns))
