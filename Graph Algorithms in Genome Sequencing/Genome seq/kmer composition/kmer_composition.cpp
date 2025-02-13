#include <iostream>
#include <string>


using std::cout;
using std::cin;
using std::endl;
using std::string;


/*
 * Computes the k-mer compositition of a string text
 *
 * \param k         integer length of k-mers to be found
 * \param text      string to split into a k-mer compositition
 *
 * \return a string with each k-mer in text separated by newlines
 */
string kmer_composition(int k, const string& text) {
    // TODO: your code here
    return "";
}


int main(int argc, char* argv[]) {
    int k;
    cin >> k;

    string text;
    cin >> text;

    cout << kmer_composition(k, text) << endl;
}
