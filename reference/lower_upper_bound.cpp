
int upperBound(int arr[], int s, int e, int target) {
    int ans = e + 1;

    while (s <= e) {
        int m = (s + e) / 2;

        if (arr[m] > target) {
            ans = m;
            e = m - 1;
        }
        else s = m + 1;
    }

    return ans;
}

int lowerBound(int arr[], int s, int e, int target) {
    int ans = e + 1;

    while (s <= e) {
        int m = (s + e) / 2;

        if (arr[m] >= target) {
            ans = m;
            e = m - 1;
        }
        else s = m + 1;
    }

    return ans;
}


