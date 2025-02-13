#python3
import sys


def find_paths(graph):
    """Finds all maximum non-branching paths in the given graph

    Args:
        graph:      a list of strings containing edges in the graph; one
                    string may correspond to multiple edges if it is of the
                    form "X -> Y,Z"

    Returns:
        a string containing all maximum non-branching paths in the format
        specified in the problem
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    graph = sys.stdin.read().strip().splitlines()
    print(find_paths(graph))
