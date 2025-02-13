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
 * Computes probability of a path pi through a given HMM.
 *
 * \param pi            a string representing the path
 * \param states        a vector of chars containing all possible states
 * \param transition    a map s.t. transition[x][y] is the probability
 *                      of transitioning from state x to state y. 
 *                      x and y are chars in states.
 *
 * \return a double with the probability to at least three significant figures
 */
double path_probability(const string& pi, const vector<char>& states, 
        const map<char,map<char,double>>& transition) {
    // TODO: your code here
    return 0.0;
}

int main(int argc, char* argv[]) {
    string pi;
    vector<char> states;
    map<char,map<char,double>> transition;

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
    cin.ignore(100, '\n'); // first line of transition matrix

    // read in transition matrix
    char curr_state;
    double curr_prob;
    while (cin >> curr_state) {
        for (char state : states) {
            cin >> curr_prob;
            transition[curr_state][state] = curr_prob;
        }
    }

    cout << path_probability(pi, states, transition) << endl;
    return 0;
}
