#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

int change_coins(int money, vector<int> coins) {
    // TODO: your code here
    return -1;
}

int main() {
    int money;
    cin >> money;

    vector<int> coins;
    int coin;

    while (cin >> coin) {
        coins.push_back(coin);
        cin.ignore(4,',');
    }

    cout << change_coins(money, coins) << endl;

    return 0;
}
