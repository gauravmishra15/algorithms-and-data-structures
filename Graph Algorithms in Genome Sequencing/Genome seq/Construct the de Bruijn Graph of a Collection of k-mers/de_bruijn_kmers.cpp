#include <iostream>
#include <vector>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;


/*
 * Creates a de Bruijn graph from a colletion of k-mers
 *
 * \param patterns      a vector of strings containing the k-mer colleciton
 *                      to be made into a de Bruijn graph
 *
 * \return a string containing an adjacency list representation of the
 * de Bruijn graph as described in the problem specification
 */
string de_bruijn(const vector<string>& patterns) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    vector<string> patterns;

    string pattern;
    while (cin >> pattern) {
        patterns.push_back(pattern);
    }

    cout << de_bruijn(patterns) << endl;
}
