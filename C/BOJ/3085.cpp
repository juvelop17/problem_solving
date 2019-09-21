#include <iostream>
#include <string>
using namespace std;

int check(char M[][50], int n) {
	int i, j, count = 0, max = 0;

	// 가로검사
	for (i = 0; i < n; i++) {
		count = 1;
		for (j = 0; j + 1 < n; j++) {
			if (M[i][j] == M[i][j + 1])
				count++;
			else
				count = 1;
			if (max < count)
				max = count;
		}
	}

	// 세로검사
	for (i = 0; i < n; i++) {
		count = 1;
		for (j = 0; j + 1 < n; j++) {
			if (M[j][i] == M[j + 1][i])
				count++;
			else
				count = 1;
			if (max < count)
				max = count;
		}
	}

	return max;
}

void print(char M[][50], int n) {
	int i, j;
	printf("\n");
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			printf("%c", M[i][j]);
		}
		printf("\n");
	}
}

int main() {
	int n, i,j,max=0,count;
	char M[50][50], prev;
	char str[50 + 1];

	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%s", str);
		for (j = 0; j < n ; j++) {
			M[i][j] = str[j];
		}
	}

	// 가로검사
	for (i = 0; i < n; i++) {
		count = 1;
		for (j = 0; j+1 < n; j++) {
			if (M[i][j] == M[i][j + 1])
				count++;
			else
				count = 1;
			if (max < count)
				max = count;
		}
	}

	// 세로검사
	for (i = 0; i < n; i++) {
		count = 1;
		for (j = 0; j + 1 < n; j++) {
			if (M[j][i] == M[j + 1][i])
				count++;
			else
				count = 1;
			if (max < count)
				max = count;
		}
	}

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			if (i + 1 < n) {
				swap(M[i][j], M[i + 1][j]);
				//print(M, n);
				count = check(M, n);
				if (max < count)
					max = count;
				swap(M[i][j], M[i + 1][j]);
				//print(M, n);
			}

			if (j + 1 < n) {
				swap(M[i][j], M[i][j + 1]);
				count = check(M, n);
				if (max < count)
					max = count;
				swap(M[i][j], M[i][j + 1]);
			}
		}

	}
	printf("%d", max);

	return 0;
}