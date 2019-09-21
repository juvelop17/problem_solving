#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int N, S;
	int i,j,num,a[21], sum;
	int count = 0;

	scanf("%d", &N);
	scanf("%d", &S);

	for (i = 0; i < N; i++) {
		scanf("%d", &a[i]);
	}

	count = 0;
	for (i = 1; i < pow(2,N); i++) {
		sum = 0;
		num = i;

		for (j = 0; j < N; j++) {
			if (num % 2 == 1) {
				sum += a[j];
			}
			num /= 2;
		}

		if (sum == S) {
			count++;
		}
	}
	printf("%d\n", count);

	return 0;
}