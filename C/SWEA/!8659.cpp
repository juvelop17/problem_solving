#include <stdio.h>


int T,K;



int GCD(int n, int a,int b){
    if (b == 0){
        return 0;
    }

    if (n == K){
        return -1;
    }
    
    return GCD(n+1,b,a%b)+1;
}


int solution(int K){
    int res;
    int MAX_VAL = 1000;
    int min_a = MAX_VAL;
    int min_b = MAX_VAL;

    for (int i=1;i<=MAX_VAL;i++){
        for (int j=1;j<=MAX_VAL;j++){
            if (j > min_a){
                continue;
            }

            res = GCD(1,j,i);
            if (res == K){
                if (j < min_a){
                    min_a = j;
                } else if (j == min_a && i < min_b){
                    min_b = i;
                }
            }
        }
    }
    
    return (min_a,min_b);
}




int main(){
    freopen("input.txt","r",stdin);
    scanf("%d",&T);
    for (int i=1;i<=T;i++){
        scanf("%d",&K);
        printf("#%d %d\n",i,solution(K));
    }

}


