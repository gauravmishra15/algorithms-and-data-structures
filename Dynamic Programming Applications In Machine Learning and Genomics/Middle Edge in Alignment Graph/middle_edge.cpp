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
 *
 * return a string middle edge's nodes
 * be sure to follow the problem's output format
 */
string middle_edge(int m, int mu, int sigma, const string& s, const string& t) {
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

    cout << middle_edge(m,mu,sigma,s,t) << endl;
    return 0;
}
