#include <iostream>
#include <string>
#include <vector>


using std::string;
using std::vector;
using std::cin;
using std::cout;
using std::endl;


/*
 * Creates a profile HMM from a multiple alignment.
 *
 * \param theta         a double threshold for the seed alignment
 * \param sigma         a vector of chars containing the HMM alphabet
 * \param alignment     a vector of strings containing the multiple alignment
 *                          for which the profile HMM will be constructed.
 *
 * \return a string with the emission and transition matrices formatted 
 * according to the problem output specification.
 */
string profile_hmm(double theta, vector<char> sigma, vector<string> alignment) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    // read in theta threshold
    double theta;
    cin >> theta;
    cin.ignore(1, '\n');    // ignore newline after theta
    cin.ignore(100, '\n');  // delimiter

    // read in HMM alphabet
    vector<char> sigma;
    char letter;
    cin >> letter;
    while (letter != '-') {
        sigma.push_back(letter);
        cin >> letter;
    }
    cin.ignore(100, '\n');  // delimiter

    // read in multiple alignment
    vector<string> alignment;
    string alignment_line;
    while (cin >> alignment_line) {
        alignment.push_back(alignment_line);
    }

    // compute the profile HMM and print it
    cout << profile_hmm(theta, sigma, alignment) << endl;

    return 0;
}
