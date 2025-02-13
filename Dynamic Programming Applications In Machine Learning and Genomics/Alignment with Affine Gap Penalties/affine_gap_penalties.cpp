#include <iostream>
#include <string>
#include <algorithm>

using std::cout;
using std::cin;
using std::endl;
using std::string;

/**
 * m, mu, sigma, and eps are the scoring parameters (eps is epsilon)
 * s and t are the strings to be aligned 
 *
 * return a string with the alignment score and the reconstructed alignment
 * be sure to follow the problem's output format
 */
string align(int m, int mu, int sigma, int eps, const string& s, const string& t) {
    // TODO: your code here
    return "";
}


int main() {
    int m,mu,sigma,eps;
    cin >> m >> mu >> sigma >> eps;
    cin.ignore();
    string s,t;
    getline(cin, s);
    getline(cin, t);

    cout << align(m,mu,sigma,eps,s,t) << endl;
    return 0;
}
