#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::getline;
using std::endl;
using std::vector;
using std::string;

/**
 * source is the integer label of the source node
 * sink is the integer label of the sink node
 * edges is a vector of the string representations of the edges from the input file
 *
 * return a string with the correct output format
 */
string longest_path(int source, int sink, vector<string> edges) {
    // TODO: your code here
    return "";
}

int main() {
    int source,sink;
    cin >> source >> sink;
    cin.ignore(256, '\n');

    vector<string> edges;

    for (string line; getline(cin, line);) {
        edges.push_back(line);
    }

    cout << longest_path(source, sink, edges) << endl;
    return 0;
}
