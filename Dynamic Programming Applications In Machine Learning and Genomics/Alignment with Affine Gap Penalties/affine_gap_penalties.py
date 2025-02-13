#python3
import sys

def align(m,mu,sigma,eps,s,t):
    """
    m, mu, and sigma are the scoring parameters (eps is epsilon)
    s and t are the strings to be aligned

    return a string with the score and reconstructed alignment
    be sure to follow the output format for this problem
    """
    # TODO: your code here
    return ""

if __name__ == "__main__":
    m,mu,sigma,eps = map(int,sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]
    print(align(m,mu,sigma,eps,s,t))
