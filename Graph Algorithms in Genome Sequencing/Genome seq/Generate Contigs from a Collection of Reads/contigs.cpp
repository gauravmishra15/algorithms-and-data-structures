#include <iostream>
#include <vector>
#include <string>


using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;


/*
 * Finds all contigs in a de Bruijn graph made from patterns
 *
 * \param patterns      a vector of strings containing all k-mers to
 *                      be used to construct the de Bruijn graph for
 *                      this problem
 *
 * \return a string with all the contigs in the format specified in the
 * problem description
 */
string contigs(const vector<string>& patterns) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    vector<string> patterns;
    string pattern;

    while (cin >> pattern) {
        patterns.push_back(pattern);
    }

    cout << contigs(patterns) << endl;
}
