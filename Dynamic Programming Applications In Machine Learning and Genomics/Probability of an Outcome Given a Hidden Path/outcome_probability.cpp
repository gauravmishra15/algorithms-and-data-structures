#include <iostream>
#include <string>
#include <vector>
#include <map>

using std::string;
using std::vector;
using std::map;
using std::cin;
using std::cout;
using std::endl;


/*
 * Computes probability of an an outcome x given a path pi and an emission matrix.
 *
 * \param x             a string outcome
 * \param sigma         a vector of chars containing the HMM alphabet
 * \param pi            a string representing the path
 * \param states        a vector of chars containing all possible states
 * \param emission      a map s.t. emission[x][y] is the probability
 *                      of emitting y from state x. x and y are characters.
 *                      x is in states, y is in sigma.
 *
 * \return a double with the probability to at least three significant figures
 */
double outcome_probability(const string& x, const vector<char>& sigma,
        const string& pi, const vector<char>& states, 
        const map<char,map<char,double>>& emission) {
    // TODO: your code here
    return 0.0;
}

int main(int argc, char* argv[]) {
    string x, pi;
    vector<char> sigma, states;
    map<char,map<char,double>> emission;

    // read in x
    cin >> x;
    cin.ignore(1, '\n'); // last newline
    cin.ignore(100, '\n'); // delimiter

    // read in sigma
    char letter;
    cin >> letter;
    while (letter != '-') {
        sigma.push_back(letter);
        cin >> letter;
    }
    cin.ignore(100, '\n'); // delimiter

    // read in pi
    cin >> pi;
    cin.ignore(1, '\n'); // last newline
    cin.ignore(100, '\n'); // delimiter

    // read in states
    char state;
    cin >> state;
    while (state != '-') {
        states.push_back(state);
        cin >> state;
    }

    cin.ignore(100, '\n'); // delimiter
    cin.ignore(100, '\n'); // first line of emission matrix

    // read in emission matrix
    char curr_state;
    double curr_prob;
    while (cin >> curr_state) {
        for (char letter : sigma) {
            cin >> curr_prob;
            emission[curr_state][letter] = curr_prob;
        }
    }

    cout << outcome_probability(x, sigma, pi, states, emission) << endl;
    return 0;
}
