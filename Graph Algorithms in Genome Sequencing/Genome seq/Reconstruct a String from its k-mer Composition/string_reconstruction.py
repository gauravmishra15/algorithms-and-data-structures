#python3
import sys

def reconstruct(k, patterns):
    """Reconstructs a string from its k-mer composition

    Args:
        k:          the length of k-mers in the k-mer composition
        patterns:   a list of strings containing the k-mer composition

    Returns:
        A string text with k-mer composition equal to patterns
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    patterns = [line.strip() for line in sys.stdin if line.strip()]

    print(reconstruct(k, patterns))
