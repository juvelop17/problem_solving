#include <string>
#include <vector>
#include <iostream>

using namespace std;


int solution(string answer_sheet, vector<string> sheets) {
    int answer = -1;

    int total_score = 0;

    for (int i=0;i<sheets.size();i++){
        for (int j=i+1;j<sheets.size();j++){
            int cnt = 0;
            int cont_cnt = 0;
            int longest_cnt = 0;
            int score;

            for(int index=0;index<answer_sheet.size();index++){
                if (answer_sheet[index] != sheets[i][index] && sheets[i][index] == sheets[j][index]) {
                    cnt += 1;
                    cont_cnt += 1;
                    if (longest_cnt < cont_cnt) {
                        longest_cnt = cont_cnt;
                    }
                } else {
                    cont_cnt = 0;
                }
            }

            score = cnt + longest_cnt * longest_cnt;

            if (score > total_score) {
                total_score = score;
            }

            // cout << cnt << " " << cont_cnt << " " << longest_cnt << " " << score << endl;
        }
    }

    answer = total_score;

    return answer;
}

int main() {
    string answer_sheet = "24551";
    vector<string> sheets;
    sheets.push_back("24553");
    sheets.push_back("24553");
    sheets.push_back("24553");
    sheets.push_back("24553");

    cout << solution(answer_sheet,sheets) << endl;
}