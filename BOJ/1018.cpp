#include <iostream>
using namespace std;

void print_matrix(char board[][50], int x, int y) {
	int i, j;

	printf("\n");
	for (i = 0; i < x; i++) {
		for (j = 0; j < y; j++) {
			printf("%c", board[i][j]);
		}
		printf("\n");
	}
	printf("\n");

}

int count(char board[][50], int x, int y) {
	int count_white, count_black;
	int i, j;

	count_white = count_black = 0;
	for (i = x; i < x + 8; i++) {
		for (j = y; j < y + 8; j++) {
			// white 시작

			// 행이 짝수
			if (i % 2 == 0) {
				// 열이 짝수
				if (j % 2 == 0) {
					if (board[i][j] != 'W') {
						count_white++;
					}
				}
				// 열이 홀수
				else {
					if (board[i][j] != 'B') {
						count_white++;
					}
				}
			}
			// 행이 홀수
			else {
				// 열이 짝수
				if (j % 2 == 0) {
					if (board[i][j] != 'B') {
						count_white++;
					}
				}
				// 열이 홀수
				else {
					if (board[i][j] != 'W') {
						count_white++;
					}
				}
			}

			// black 시작
			// 행이 짝수
			if (i % 2 == 0) {
				// 열이 짝수
				if (j % 2 == 0) {
					if (board[i][j] != 'B') {
						count_black++;
					}
				}
				// 열이 홀수
				else {
					if (board[i][j] != 'W') {
						count_black++;
					}
				}
			}
			// 행이 홀수
			else {
				// 열이 짝수
				if (j % 2 == 0) {
					if (board[i][j] != 'W') {
						count_black++;
					}
				}
				// 열이 홀수
				else {
					if (board[i][j] != 'B') {
						count_black++;
					}
				}
			}
		}
	}

	if (count_white < count_black) {
		return count_white;
	}
	else {
		return count_black;
	}
}

int main() {
	int x, y;
	int width, height;
	char board[50][50];
	int i, j, min=10000, result;
	char str[50+1];

	scanf("%d ", &width);
	scanf("%d ", &height);

	for (i = 0; i < width; i++) {
		scanf("%s", str);
		for (j = 0; j < height; j++) {
			board[i][j] = str[j];
		}
	}

	//print_matrix(board, width, height);

	for (i = 0; i < width; i++) {
		for (j = 0; j < height; j++) {
			if (i + 7 <= width && j +7 <=height) {
				result = count(board, i, j);
				if (min > result) {
					min = result;
				}
			}
		}
	}

	printf("%d", min);
}