#python3
import sys


def de_bruijn(k, text):
    """Creates a de Bruijn graph from a string given a value of k

    Args:
        k:          the length of strings represented by edges in the
                    de Bruijn graph
        text:       the string from which the de Bruijn grpah will be
                    constructed

    Returns:
        a string containing an adjacency list representation of the de Bruijn
        graph as described in the problem specification
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    text = sys.stdin.readline().strip()

    print(de_bruijn(k, text))
