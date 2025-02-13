#include <iostream>
#include <vector>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;


/*
 * Creates an overlap graph from a list of k-mers
 *
 * \param patterns      a vector of string k-mers
 *
 * \return a string containing an adjacency list representation of the
 * overlap graph as described in the problem specification
 */
string overlap_graph(const vector<string>& patterns) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    vector<string> patterns;

    string pattern;
    while (cin >> pattern) {
        patterns.push_back(pattern);
    }

    cout << overlap_graph(patterns) << endl;
}
