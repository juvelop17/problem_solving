#include<iostream>

using namespace std;


//  (1 2 3 4 5 6) -> 
//  (6 2 3 4 5 1) -> 
//  (2 6 3 4 5 1) -> 
//  (1 6 3 4 5 2) -> 
//  (1 6 3 5 4 2) -> 
//  (1 6 5 3 4 2) -> 
//  (1 6 5 4 3 2)



int n;
int min_cnt;
int mp[32767];


int swap(int arr[], int i,int j){
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;

    return 0;
}

bool check(){
    bool res = true;
    int num = mp[0];
    for(int i=1;i<n-1;i++){
        if (num == 1) {
            num = n;
        }
        
        if (mp[i] == num) {
            num--;
        } else {
            res = false;
            break;
        }
    }
    return res;
}

void display(int cnt) {
    cout << cnt << endl;
    for (int i=0;i<n;i++){
        cout << mp[i] << " ";
    }
    cout << endl;
}

int move(int cnt){
    display(cnt);

    if (cnt > n || cnt > min_cnt) {
        return 0;
    }

    if (check() && cnt < min_cnt) {
        min_cnt = cnt;
    }

    for(int i=0;i<n;i++){
        swap(i,i+1);
        move(cnt+1);
        swap(i,i+1);
    }

    return 0;
}


int solution(){
    for(int i=0;i<n;i++){
        mp[i] = i+1;
    }

    min_cnt = n+1;
    move(0);

    return min_cnt;
}

int main(){
    freopen("input.txt","r",stdin);

    cin >> n;
    cout << solution();
    return 0;
}