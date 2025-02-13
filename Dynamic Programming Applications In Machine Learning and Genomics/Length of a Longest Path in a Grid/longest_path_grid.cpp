#include <iostream>
#include <algorithm>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

using matrix = vector<vector<int>>;

int longest_path(int n, int m, matrix down, matrix right) {
    // TODO: your code here
    return -1;
}

int main() {
    int n,m;
    cin >> n;
    cin >> m;

    matrix down;
    for (int i = 0; i < n; i++) {
        vector<int> curr(m+1);
        for (int j = 0; j < m+1; j++) {
            cin >> curr[j];
        }
        down.push_back(curr);
    }

    cin.ignore(256,'-');

    matrix right;
    for (int i = 0; i < n+1; i++) {
        vector<int> curr(m);
        for (int j = 0; j < m; j++) {
            cin >> curr[j];
        }
        right.push_back(curr);
    }

    cout << longest_path(n,m,down,right) << endl;
    return 0;
}
