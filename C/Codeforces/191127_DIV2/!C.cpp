#include <iostream>

using namespace std;

long long t, r, b, k;

long long gcd(long long a, long long b)
{
	long long c;
	while (b != 0)
	{
		c = a % b;
		a = b;
		b = c;
	}
	return a;
}

long long lcm(long long a, long long b)
{
    return a * b / gcd(a, b);
}

long long solution() {
    long long mx = max(r,b);
    long long mn = min(r,b);

    if ((mx - 2 * gcd(mx,mn)) / mn > k - 1)  < max(r,b)) {
        return 0;
    }
    
    return 1;
}

int main() {
    cin >> t;
    for (int test_case=1;test_case<=t;test_case++){
        cin >> r >> b >> k;

        cout << (solution() ? "OBEY" : "REBEL") << endl;
    }

    return 0;
}
