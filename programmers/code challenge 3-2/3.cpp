#include <iostream>



#include <string>
#include <vector>
#include <algorithm>


using namespace std;





long long solution(int n, int m, int x, int y, vector<vector<int>> queries) {
    long long answer = -1;

    vector<vector<int>> ver;
    vector<vector<int>> hor;

//    int ver = 0;
//    int vi = -1;
//    int hor = 0;
//    int hi = -1;

    for (int i = 0; i < queries.size(); i++) {
        if (queries[i][0] == 0) {
            ver.push_back(queries[i]);
        } else if (queries[i][0] == 1) {
            ver.push_back(queries[i]);
        } else if (queries[i][0] == 2) {
            hor.push_back(queries[i]);
        } else {
            hor.push_back(queries[i]);
        }
    }

    int vsum = 0;
    int vidx = 0;
    int vmax = 0;
    int vmin = 0;
    for (int i = 0; i < ver.size(); i++) {
        if (ver[i][0] == 0) {
            vsum -= ver[i][1];
        } else {
            vsum += ver[i][1];
        }
        if (vsum >= n) {
            vsum = n - 1;
            vidx = i + 1;
        } else if (vsum <= -n) {
            vsum = -n + 1;
            vidx = -(i + 1);
        }

        if (vmax < vsum) vmax = vsum;
        if (vmin > vsum) vmin = vsum;
    }

    int hsum = 0;
    int hidx = 0;
    int hmax = 0;
    int hmin = 0;
    for (int i = 0; i < ver.size(); i++) {
        if (ver[i][0] == 0) {
            hsum -= ver[i][1];
        } else {
            hsum += ver[i][1];
        }
        if (hsum >= m) {
            hsum = m - 1;
            hidx = i + 1;
        } else if (hsum <= -m) {
            hsum = -m + 1;
            hidx = -(i + 1);
        }
        if (hmax < hsum) {
            hmax = hsum;
        }
        if (hmin > hsum) {
            hmin = hsum;
        }
    }

    int vs = 0;
    if (vidx < 0) {
        vs = n - 1;
        vidx *= -1;
    }

    for (int i = vidx; i < ver.size(); ++i) {

    }


    return answer;
}



int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("input.txt", "r", stdin);

    int n = 2;
    int m = 2;
    int x = 0;
    int y = 0;
    vector<vector<int>> queries = {{2,1},{0,1},{1,1},{0,1},{2,1}};

    cout << solution(n, m, x, y, queries);




    return 0;
}