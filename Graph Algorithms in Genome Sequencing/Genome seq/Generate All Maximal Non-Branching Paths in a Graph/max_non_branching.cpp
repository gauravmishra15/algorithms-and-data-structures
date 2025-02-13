#include <iostream>
#include <vector>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;
using std::getline;


/*
 * Finds all maximum non-branching paths in the given graph
 *
 * \param graph     a vector of strings containing edges in the graph;
 *                  one string may correspond to multiple edges if it
 *                  is of the form "X -> Y,Z"
 *
 * \return a string containing all maximum non-branching paths in the
 * format specified by the problem.
 */
string find_paths(const vector<string>& graph) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    vector<string> graph;

    string line;
    while (getline(cin, line, '\n')) {
        graph.push_back(line);
    }

    cout << find_paths(graph) << endl;
}
