#python3
import sys


def reconstruct_string(patterns):
    """Reconstructs a string from its genome path

    Args:
        patterns:       a list of string k-mers in the order they appear in
                        text

    Returns:
        a string text with the given genome path
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    patterns = sys.stdin.read().strip().splitlines()
    print(reconstruct_string(patterns))
