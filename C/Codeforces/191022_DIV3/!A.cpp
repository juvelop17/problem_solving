#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

// No two students 𝑖 and 𝑗 such that |𝑎𝑖−𝑎𝑗|=1 belong to the same team (i.e. skills of each pair of students in the same team have the difference strictly greater than 1);
// the number of teams is the minimum possible.

int q, n;
int arr[100];
vector< vector<int> > vec;

void quickSort(int arr[], int left, int right)
{
    int L = left, R = right;
    int temp;
    int pivot = arr[(left + right) / 2];
    while (L < R)
    {
        while (arr[L] < pivot)
            L++;
        while (arr[R] > pivot)
            R--;
        if (L <= R)
        {
            if (L < R)
            {
                temp = arr[L];
                arr[L] = arr[R];
                arr[R] = temp;
            }
            L++;
            R--;
        }
    }

    if (left < R)
        quickSort(arr, left, R);
    if (right > L)
        quickSort(arr, L, right);
}

void printArray(int arr[])
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void printVector(vector< vector<int> > vec)
{
    for (int i = 0; i < vec[i].size(); i++)
    {   
        for (int j = 0; j<vec[i].size();j++){
            printf("%d ", vec[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}


int solution()
{
    quickSort(arr, 0, n-1);

    int new_num,comp_num,cnt;

    cnt = 0;
    for (int i=0;i<n-1;i++){
        new_num = arr[i];

        bool is_added = false;
        for (int j=0;j<vec.size();j++){
            comp_num = vec[j][vec[j].size()-1];
            if (abs(new_num-comp_num) != 1){
                vec[j].push_back(new_num);
                is_added = true;
                break;
            }
        }
        if (is_added == false){
            vector<int> _vec;
            vec.push_back(_vec);
            vec[vec.size()-1].push_back(new_num);
            cnt++;
        }
    }
    printArray(arr);
    printVector(vec);
    return cnt;
}

int main()
{
    freopen("input.txt", "r", stdin);

    scanf("%d", &q);

    for (int i = 0; i < q; i++)
    {
        scanf("%d", &n);
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &arr[j]);
        }
        printf("%d\n",solution());
    }
}
