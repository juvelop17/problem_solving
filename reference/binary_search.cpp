
int binarySearch(int arr[], int s, int e, int target) {
    while (s <= e) {
        int m = (s + e) / 2;

        if (arr[m] == target) return m;
        else if (arr[m] < target) s = m + 1;
        else s = m - 1;
    }

    return -1;
}


