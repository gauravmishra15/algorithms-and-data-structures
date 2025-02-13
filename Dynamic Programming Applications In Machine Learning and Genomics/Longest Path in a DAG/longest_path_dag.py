#python3
import sys

def longest_path(source, sink, edges):
    """
    source is the integer source node label
    sink is the integer sink node lable
    edges is a string list of the edges from the input file
    
    return a string containing the output in the correct format
    """
    # TODO: your code here
    return ""

if __name__ == "__main__":
    source = int(sys.stdin.readline().strip())
    sink = int(sys.stdin.readline().strip())
    edges = [line.strip() for line in sys.stdin]

    print(longest_path(source,sink,edges))
