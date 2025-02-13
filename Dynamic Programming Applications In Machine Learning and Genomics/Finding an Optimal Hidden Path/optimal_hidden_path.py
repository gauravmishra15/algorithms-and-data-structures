#python3
import sys

def optimal_path(x,sigma,states,transition,emission):
    """Computes the optimal path through an HMM given an emitted string

    Args:
        x: A string containing the outcome
        sigma: A list of strings containing the HMM alphabet
        states: A list of strings containing all possible states
        transition: A 2D dictionary s.t. transition[x][y] is the
            probability of transitioning from state x to state y.
        emission: A 2D dictionary s.t. emission[x][y] is the
            probability of emitting letter y from state x.

    Returns:
        A string containing the optimal path
    """
    # TODO: your code here
    return ""

if __name__ == "__main__":
    x = sys.stdin.readline().strip()
    sys.stdin.readline() # delimiter

    sigma = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    states = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    chars = sys.stdin.readline().strip().split() 
    transition = [sys.stdin.readline().strip().split() for _ in range(len(states))]
    transition = {line[0]:dict(zip(chars, map(float,line[1:]))) for line in transition}
    sys.stdin.readline() # delimiter

    chars = sys.stdin.readline().strip().split() 
    emission = [sys.stdin.readline().strip().split() for _ in range(len(states))]
    emission = {line[0]:dict(zip(chars, map(float,line[1:]))) for line in emission}

    print(optimal_path(x,sigma,states,transition,emission))
