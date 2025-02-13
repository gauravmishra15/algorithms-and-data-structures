#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iterator>
#include <sstream>

using std::string;
using std::vector;
using std::map;
using std::cin;
using std::cout;
using std::endl;

/*
 * Computes the optimal path through the HMM given an emitted string
 *
 * \param x             a string emitted string
 * \param sigma         a vector of chars containing the HMM alphabet
 * \param states        a vector of chars containing all possible states
 * \param transition    a map s.t. transition[x][y] is the probability
 *                      of transitioning from state x to state y. 
 *                      x and y are characters in states.
 * \param emission      a map s.t. emission[x][y] is the probability
 *                      of emitting y from state x. x and y are characters.
 *                      x is in states, y is in sigma.
 *
 * \return a string representing the optimal decoded path
 */
string optimal_path(const string& x, const vector<char>& sigma, 
        const vector<char>& states, const map<char,map<char,double>>& transition,
        const map<char,map<char,double>>& emission) {
    // TODO: your code here
    return "";
}

int main(int argc, char* argv[]) {
    string x;
    vector<char> sigma, states;
    map<char,map<char,double>> emission, transition;

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

    // read in states
    char state;
    cin >> state;
    while (state != '-') {
        states.push_back(state);
        cin >> state;
    }

    cin.ignore(100, '\n'); // delimiter
    cin.ignore(100, '\n'); // first line of transition matrix
    char curr_state;
    double curr_prob;

    // read in transition matrix
    for (char state : states) {
        cin >> curr_state;
        for (char other_state : states) {
            cin >> curr_prob;
            transition[curr_state][other_state] = curr_prob;
        }
    }
    
    cin.ignore(1, '\n'); // transition last newline
    cin.ignore(100, '\n'); // delimiter
    cin.ignore(100, '\n'); // first line of emission matrix

    // read in emission matrix
    for (char state : states) {
        cin >> curr_state;
        for (char letter : sigma) {
            cin >> curr_prob;
            emission[curr_state][letter] = curr_prob;
        }
    }

    cout << optimal_path(x, sigma, states, transition, emission) << endl;
    return 0;
}
