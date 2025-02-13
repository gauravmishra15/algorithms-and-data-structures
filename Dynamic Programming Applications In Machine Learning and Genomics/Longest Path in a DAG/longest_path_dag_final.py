#python3
import sys
import networkx as nx

def calc_dist(graph, path):
    dist = 0
    for i in xrange(len(path)-1):
        dist += graph[path[i]][path[i+1]]['weight']

    return dist

def find_longest_path(src, sink, graph):
    paths = nx.all_simple_paths(graph, source=src, target=sink)
    longest_path = []
    max_dist = 0
    for path in paths:
        dist = calc_dist(graph, path)
        if dist > max_dist:
            max_dist = dist
            longest_path = path

    return max_dist, longest_path

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

    #print(longest_path(source,sink,edges))
    graph = nx.DiGraph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=edge[2])

    dist, path = find_longest_path(src, sink, graph)
    print dist
    print "->".join([str(path[i]) for i in xrange(len(path))])
