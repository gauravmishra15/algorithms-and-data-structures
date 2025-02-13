#include <iostream>
#include <vector>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;


/*
 * Reconstructs a string from its genome path
 *
 * \param patterns      a vector of string k-mers in the order they appear
 *                      in text
 *
 * \return a string text with the given genome path
 */
string reconstruct_string(const vector<string>& patterns) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    vector<string> patterns;

    string pattern;
    while (cin >> pattern) {
        patterns.push_back(pattern);
    }

    cout << reconstruct_string(patterns) << endl;
}
