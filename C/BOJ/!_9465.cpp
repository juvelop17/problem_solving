#include <iostream>

using namespace std;


int T,n;
int memory_arr[3][100000] = {-1};
int map_arr[3][100000] = {-1};



void printMap(int map_arr[][100000]){
    for (int i=0;i<3;i++){
        for (int j=0;j<n;j++){
            cout << map_arr[i][j] << "\t";
        }
        cout << endl;
    }
}


int solution(){
    printMap(map_arr);
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    freopen("input.txt", "r", stdin);  
    
    cin >> T;
    for (int i=0;i<T;i++){
        cin >> n;
        for(int j=0;j<2;j++){
            for(int k=0;k<n;k++){
                cin >> map_arr[j][k];
            }
        }
        printMap(map_arr);
    }



    return 0;
}







