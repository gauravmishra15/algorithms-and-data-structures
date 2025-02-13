#python3
import sys

def kmer_composition(k, text):
    """Computes the k-mer composition of string text

    Args:
        k:          integer length of k-mers to be found
        text:       string to split into a k-mer composition

    Returns:
        a string with each k-mer in text separated by newlines
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    text = sys.stdin.readline().strip()

    print(kmer_composition(k, text))
