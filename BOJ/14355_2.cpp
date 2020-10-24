#include <stdio.h>  
#include <algorithm>  
#include <assert.h>
#include <bitset>
#include <cmath>  
#include <complex>  
#include <deque>  
#include <functional>  
#include <iostream>  
#include <limits.h>  
#include <map>  
#include <math.h>  
#include <queue>  
#include <set>  
#include <stdlib.h>  
#include <string.h>  
#include <string>  
#include <time.h>  
#include <unordered_map>  
#include <unordered_set>  
#include <vector>  

#pragma warning(disable:4996)  
#pragma comment(linker, "/STACK:336777216")  
using namespace std;

#define mp make_pair  
#define Fi first  
#define Se second  
#define pb(x) push_back(x)  
#define szz(x) ((int)(x).size())  
#define rep(i, n) for(int i=0;i<n;i++)  
#define all(x) (x).begin(), (x).end()  
#define ldb ldouble  

typedef tuple<int, int, int> t3;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <db, db> pdd;

int IT_MAX = 1 << 20;
const ll MOD = 1000000007;
const int INF = 0x3f3f3f3f;
const ll LL_INF = 0x3f3f3f3f3f3f3f3f;
const db PI = acos(-1);
const db EPS = 1e-10;

char getwinner(char a, char b) {
	if (a > b) swap(a, b);
	if (a == 'P' && b == 'R') return 'P';
	if (a == 'P' && b == 'S') return 'S';
	return 'R';
}

vector <char> Vl;
int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, R, P, S, i, j;
		scanf("%d %d %d %d", &N, &R, &P, &S);
		
		Vl.clear();
		for (i = 0; i < P; i++) Vl.push_back('P');
		for (i = 0; i < R; i++) Vl.push_back('R');
		for (i = 0; i < S; i++) Vl.push_back('S');

		bool chk = false;
		do {
			vector <char> V1;
			vector <char> V2;
			V1 = Vl;

			while (V1.size() > 1) {
				int i;
				V2.clear();
				for (i = 0; i < V1.size(); i += 2) {
					if (V1[i] == V1[i + 1]) break;
					V2.push_back(getwinner(V1[i], V1[i + 1]));
				}
				if (i < V1.size()) break;

				V1 = V2;
			}
			if (V1.size() == 1) {
				chk = true;
				break;
			}
		} while (next_permutation(all(Vl)));
		
		printf("Case #%d: ", tc);
		if (chk) for (auto it : Vl) printf("%c", it);
		else printf("IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}
