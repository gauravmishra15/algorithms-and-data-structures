#include <iostream>
#include <string>
#include <vector>


using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;
using std::getline;


/*
 * Reconstructs a string from its gapped genome path
 *
 * \param k             length of k-mers
 * \param d             length of gap
 * \param paired_comp   vector of strings containing the gapped genome path
 *
 * \return a string with the appropriate gapped genome path
 */
string reconstruct(int k, int d, vector<string> paired_comp) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    int k, d;
    cin >> k >> d;
    cin.ignore(1, '\n'); // ignore extra newline

    vector<string> paired_comp;
    string line;

    while(getline(cin, line, '\n')) {
        paired_comp.push_back(line);
    }

    cout << reconstruct(k, d, paired_comp) << endl;
}
