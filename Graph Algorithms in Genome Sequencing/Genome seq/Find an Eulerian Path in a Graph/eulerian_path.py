#python3
import sys


def eulerian_path(graph):
    """Finds an Eulerian path in the given graph

    Args:
        graph:      a list of strings containing edges in the graph; one
                    string may correspond to multiple edges if it is of the
                    form "X -> Y,Z"

    Returns:
        a string containing an Eulerian path through the given graph
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    graph = sys.stdin.read().strip().splitlines()
    print(eulerian_path(graph))
