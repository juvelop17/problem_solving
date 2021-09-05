//
// Created by Junho Kim on 2021/08/17.
//

void qsort(int l, int r) {
    if (l >= r) return;

    int s = l; int e = r;
    int pivot = arr[(l + r) / 2];

    while (s <= e) {
        while (arr[s] > pivot) s++;
        while (arr[e] < pivot) e--;
        if (s <= e) {
            int temp;
            temp = arr[s];
            arr[s] = arr[e];
            arr[e] = temp;
            s++; e--;
        }
    }
    qsort(l, e);
    qsort(s, r);
}

