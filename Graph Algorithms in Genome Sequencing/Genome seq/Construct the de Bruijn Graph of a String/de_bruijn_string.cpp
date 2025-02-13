#include <iostream>
#include <vector>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;


/*
 * Creates a de Bruijn graph from a string given a value of k
 *
 * \param k         the length of strings represented by edges in the 
 *                  de Bruijn graph
 * \param text      the string from which the de Bruijn graph will be 
 *                  constructed
 *
 * \return a string containing an adjacency list representation of the
 * de Bruijn graph as described in the problem specification
 */
string de_bruijn(int k, const string& text) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    int k;
    cin >> k;

    string text;
    cin >> text;

    cout << de_bruijn(k, text) << endl;
}
