#include <iostream>
#include <string>
#include <algorithm>

using std::cout;
using std::cin;
using std::endl;
using std::string;

/**
 * m, mu, and sigma are the scoring parameters
 * s and t are the strings to be aligned
 * t will be fit into s
 *
 * return a string with the alignment score and the reconstructed alignment
 * be sure to follow the problem's output format
 */
string align(int m, int mu, int sigma, const string& s, const string& t) {
    // TODO: your code here
    return "";
}


int main() {
    int m,mu,sigma;
    cin >> m >> mu >> sigma;
    cin.ignore();
    string s,t;
    getline(cin, s);
    getline(cin, t);

    cout << align(m,mu,sigma,s,t) << endl;
    return 0;
}
