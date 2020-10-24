#include <iostream>
#include <cstdio>


using namespace std;

int q,n,num_arr[100],index_arr[101];


void printArray(){
    for(int i=0;i<n;i++){
        cout << num_arr[i] << " ";
    }
    cout << endl;
}


int solution(){
    int num_index,curr_index, temp;

    int memory_arr[100] = {0};
    if (index_arr[1] == 0){
        memory_arr[0] = 1;
    }

    for(int i=1;i<n+1;i++){
        curr_index = index_arr[i];
        if (memory_arr[curr_index] == 1){
            memory_arr[curr_index+1] = 1;
            continue;
        }

        while(!memory_arr[curr_index] && curr_index > 0){
            memory_arr[curr_index] = 1;

            temp = num_arr[curr_index];
            num_arr[curr_index] = num_arr[curr_index-1];
            num_arr[curr_index-1] = temp;

            index_arr[num_arr[curr_index-1]]--;
            index_arr[num_arr[curr_index]]++;

            curr_index--;
        }
    }
    printArray();

    return 0;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    // freopen("input.txt","r",stdin);

    cin >> q;
    for (int i=0;i<q;i++){
        cin >> n;
        for (int j=0;j<n;j++){
            cin >> num_arr[j];
            index_arr[num_arr[j]] = j;
        }
        solution();
    }

    return 0;
}

