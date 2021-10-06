
#include <iostream>


using namespace std;

long long solution(int price, int money, int count)
{
    long long sum = 0;
    int i;
    for (i = 0; i < count; ++i) {
        sum += price * (i + 1);
    }

    if (sum < money) {
        return 0;
    }

    return sum - money;
}



int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int price = 3;
    int money = 20;
    int count = 4;

    cout << solution(price, money, count);

    return 0;
}