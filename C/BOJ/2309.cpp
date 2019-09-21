
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n = 9;

int check(int m[], int *a, int *b) {
	int all_sum = 0;

	for (int i = 0; i < n; i++) {
		all_sum += m[i];
	}

	for (int i = 0; i < 9; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (all_sum - m[i] - m[j] == 100) {
				*a = i;
				*b = j;
				return 1;
			}
		}
	}

	return 0;
}


int main() {
	int m[9];
	int a, b;
	
	for (int i = 0; i < n; i++) {
		cin >> m[i];
	}

	//cout << "m : " << m << endl;
	//cout << "m + 1 : " << m + 1 << endl;
	//cout << "*(m + 1) : " << *(m + 1) << endl;
	//cout << "m + sizeof(int) * 1 : " << m + sizeof(int) * 1 << endl;
	//cout << "m + sizeof(int) * 1 : " << *(m + sizeof(int) * 1) << endl;

	sort(m, m + 9);

	//for (int i = 0; i < n; i++) {
	//	cout << m[i] << endl;
	//}

	
	check(m, &a, &b);


	for (int i = 0; i < n; i++) {
		if(i != a && i != b)
			cout << m[i] << endl;
	}

	return 0;
}

