#include <iostream>
using namespace std;


int main() {
	int sum, n, _a, count=0, i;

	scanf("%d", &n);
	_a = n;
	while (_a) _a /= 10, count++;
	

	for (i = n - 9 * count; i < n; i++) {
		sum = i;

		for (int j = i; j ; j/=10) {
			sum += j % 10;
		}
		if (sum == n) {
			printf("%d", i);
			break;
		}
	}

	if (sum != n) {
		printf("%d", 0);
	}

	return 0;
}