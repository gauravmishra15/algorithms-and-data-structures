#python3
import sys


def contigs(patterns):
    """Finds all contigs in a de Bruijn graph made from patterns

    Args:
        patterns:       a list of strings containing all k-mers to
                        be used to construct a de Bruijn graph

    Returns:
        a string with all the contigs in the format specified by
        the problem description
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    patterns = [line.strip() for line in sys.stdin if line.strip()]

    print(contigs(patterns))
