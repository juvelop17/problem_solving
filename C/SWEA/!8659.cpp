#include <stdio.h>


int T,K;
int MAX_VAL = 100000;
int min_a = MAX_VAL;
int min_b = MAX_VAL;
int prime_num[10000] = {0};


void getPrimeNum(){
    
}


int GCD(int n, int a,int b){
    if (b == 0){
        return -1;
    }

    if (n == K){
        if (a%b == 0){
            return 0;
        } else {
            return -1;
        }
    }

    return GCD(n+1,b,a%b);
}


int solution(){
    int res;
    min_a = MAX_VAL;
    min_b = MAX_VAL;

    for (int i=2;i<=MAX_VAL;i++){
        // printf("%d",i);
        if (i > min_a){
            break;
        }

        for (int j=1;j<i;j++){
            res = GCD(1,i,j);
            // printf("%d",res);
            if (res != -1){
                min_a = i;
                min_b = j;
            }
        }
    }
    
    return 0;
}


int main(){
    freopen("input.txt","r",stdin);

    scanf("%d",&T);
    for (int i=1;i<=T;i++){
        scanf("%d",&K);
        solution();
        printf("#%d %d %d\n",i,min_a,min_b);
    }

    return 0;
}


