#include <iostream>
using namespace std;

bool find_answer(int test_case[][5], int test_case_num, int num[]) {
	int ball, strike, i;
	int a1, a2, a3;

	for (i = 0; i < test_case_num; i++) {
		strike = 0;
		ball = 0;

		for (a1 = 0; a1 < 3; a1++) {
			for (a2 = 0; a2 < 3; a2++) {
				if (num[a1] == test_case[i][a2]) {
					if (a1 == a2) {
						strike++;
					}
					else {
						ball++;
					}
				}
			}
		}

		if (strike != test_case[i][3] || ball != test_case[i][4])
			return false;
	}

	return true;
}

int main() {
	int i, j, k;
	int num[3], answer_count=0;
	int test_case_num, test_case[1000][5];

	scanf("%d", &test_case_num);
	for (i = 0; i < test_case_num; i++) {
		scanf("%1d%1d%1d %1d %1d",
			&test_case[i][0],
			&test_case[i][1],
			&test_case[i][2],
			&test_case[i][3],
			&test_case[i][4]);
	}

	for (i = 1; i <= 9; i++) {
		for (j = 1; j <= 9; j++) {
			for (k = 1; k <= 9; k++) {
				if (i != j && j != k && k != i) {
					num[0] = i;
					num[1] = j;
					num[2] = k;

					if (find_answer(test_case, test_case_num, num))
						answer_count++;
				}
			}
		}
	}
	printf("%d", answer_count);

	return 0;
}