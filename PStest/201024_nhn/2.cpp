#include <iostream>
#include <sstream>

using namespace std;
int height[100] = {0};
int sum = 0;

void solution(int day, int width, int **blocks) {
  // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
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

struct input_data {
  int day;
  int width;
  int **blocks;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.day;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.width;

  inputData.blocks = new int*[inputData.day];
  for (int i = 0; i < inputData.day; i++) {
    getline(cin, line);
    iss.clear();
    iss.str(line);
    inputData.blocks[i] = new int[inputData.width];
    for (int j = 0; j < inputData.width; j++) {
      iss >> inputData.blocks[i][j];
    }
  }
}

int main() {
    // freopen("input.txt","r",stdin);

	struct input_data inputData;
	process_stdin(inputData);

	solution(inputData.day, inputData.width, inputData.blocks);
	return 0;
}