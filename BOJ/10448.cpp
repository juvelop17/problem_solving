#include <iostream>
using namespace std;

int binary_search(int tn[], int end_index, int num) {
	int start, end, mid;

	start = 1;
	end = end_index;

	while (start <= end) {
		mid = (start + end) / 2;
		if (num > tn[mid]) {
			start = mid + 1;
		}
		else if (num < tn[mid]) {
			end = mid - 1;
		}
		else {
			break;
		}
	}

	return mid;
}

bool eureka(int tn[], int end_index, int num) {
	int limit_index, sum;

	limit_index = binary_search(tn, end_index, num);

	for (int a1 = 1; a1 <= limit_index; a1++) {
		for (int a2 = a1; a2 <= limit_index; a2++) {
			for (int a3 = a2; a3 <= limit_index; a3++) {
				sum = tn[a1] + tn[a2] + tn[a3];
				if (sum == num) {
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
	int limit_index, tn[1000], num[1000], tc_num,i,end_index, sum;
	int start, end;
	bool result;

	scanf("%d", &tc_num);
	for (i = 0; i < tc_num; i++) {
		scanf("%d", &num[i]);
	}
	i = 0;
	tn[1] = 1;
	

	while(tn[i] <= 1000) {
		i++;
		tn[i] = i * (i + 1) / 2;
	}

	end_index = i;

	sum = 0;
	for (i = 0; i < tc_num; i++) {
		result = eureka(tn, end_index, num[i]);

		if (result) {
			printf("%d\n", 1);
		}
		else {
			printf("%d\n", 0);
		}
	}

	return 0;
}


