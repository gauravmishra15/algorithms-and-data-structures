#include <iostream>
#include <string>
#include <vector>


using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;


/*
 * Reconstructs a string from its k-mer composition
 *
 * \param k         the length of the k-mers in the composition
 * \param patterns  a vector of strings containing the k-mer composition
 *
 * \return a string text with k-mer composition equal to patterns
 */
string reconstruct(int k, const vector<string>& patterns) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    int k;
    cin >> k;

    vector<string> patterns;
    string pattern;

    while (cin >> pattern) {
        patterns.push_back(pattern);
    }

    cout << reconstruct(k, patterns) << endl;
}
