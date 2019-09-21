#include <cstdio>
using namespace std;

int i;

int func(int num) {
	if (num < 2) return 0;
	int a1 = func(num / 3) + num % 3 + 1;
	int a2 = func(num / 2) + num % 2 + 1;

	return a1 < a2 ? a1 : a2;
}


int main() {
	int num;

	scanf("%d", &num);
	printf("%d", func(num));
}