#python3
import sys


def de_bruijn(patterns):
    """Creates a de Bruijn graph from a collection of k-mers

    Args:
        patterns:       a list of strings containing the k-mer collecion
                        to be made into a de Bruijn graph

    Returns:
        a string containing an adjacency list representation of the de Bruijn
        graph as described in the problem specification
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    patterns = sys.stdin.read().strip().splitlines()

    print(de_bruijn(patterns))
