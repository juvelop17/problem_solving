#include <iostream>
#include <sstream>

using namespace std;
int height[500] = {0};
int sum = 0;

int H, W;
int answer;
void solution(int day, int width, int** blocks) {
   for (int i=0;i<day;i++){
        // 벽돌 쌓기
        for (int j=0;j<width;j++){
            height[j] += blocks[i][j];
        }

        // 시멘트 붓기
        int cur_pos = 0;
        int cur_height = height[0];
        while (cur_pos < width){
            int next_pos = cur_pos + 1;
            int next_height = height[next_pos];
            
            if (cur_pos >= width - 2) {
                break;
            }

            if (cur_height <= next_height) {
                cur_pos = next_pos;
                cur_height = height[cur_pos];
                continue;
            }

            next_pos += 1;
            next_height = height[next_pos];
            int max_next_pos = -1;
            int max_next_height = -1;
            while (next_pos < width){
                if (next_height > max_next_height) {
                    max_next_pos = next_pos;
                    max_next_height = next_height;
                    if (cur_height <= next_height){
                        break;
                    }
                }
                next_pos++;
                next_height = height[next_pos];
            }
            next_pos = max_next_pos;
            next_height = max_next_height;
            
            int area = (next_pos - cur_pos - 1) * min(cur_height,next_height);
            for (int h = cur_pos + 1;h < next_pos;h++){
                area -= height[h];
            }
            sum += area;

            for (int h = cur_pos + 1;h < next_pos;h++){
                height[h] = min(cur_height,next_height);
            }

            cur_pos = next_pos;
            cur_height = height[cur_pos];
        }
    }

    cout << sum << endl;
}


int main() {
   
   ios::sync_with_stdio(false);
   cin.tie(0), cout.tie(0);
   freopen("input.txt", "r", stdin);
   cin >> H >> W; int** arr;arr= new int* [1];
   arr[0] = new int[W];
   for (int i = 0; i < W; i++)cin >> arr[0][i];
   solution(1,W,arr);
   
   


   return 0;
}