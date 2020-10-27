#include <iostream>
#include <sstream>
#include <map>

using namespace std;
char line[26];
bool fast_players[26];
int cnt_players[26];

void solution(int numOfAllPlayers, int numOfQuickPlayers, char *namesOfQuickPlayers, int numOfGames, int *numOfMovesPerGame) {
  // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
    for (int i=0;i<numOfAllPlayers-1;i++){
        line[i] = 'B' + i;
    }
    for (int i=0;i<numOfAllPlayers;i++){
        fast_players[i] = false;
        cnt_players[i] = 0;
    }

    for (int i=0;i<numOfQuickPlayers;i++){
        char cur = namesOfQuickPlayers[i];
        fast_players[cur - 'A'] = true;
    }

    int cur_pos = 0;
    char cur_player = 'A';
    cnt_players[0] = 1;

    for (int round=0;round<numOfGames;round++){
        int cur_move = numOfMovesPerGame[round];
        cur_pos = (cur_pos + cur_move) % (numOfAllPlayers - 1);
        if (cur_pos < 0) {
            cur_pos = numOfAllPlayers - 1 + cur_pos;
        }
        
        char next_player = line[cur_pos];
        if (!fast_players[next_player - 'A']) {
            line[cur_pos] = cur_player;
            cur_player = next_player;
        }
        cnt_players[cur_player - 'A'] += 1;
    }

    for (int i=0;i<numOfAllPlayers-1;i++){
        cout << line[i] << " " << cnt_players[line[i]-'A'] << endl;
    }
    cout << cur_player << " " << cnt_players[cur_player-'A'] << endl;

}





//////////////////////////////////////////////////////////////////////////////

struct input_data {
  int numOfAllPlayers;
  int numOfQuickPlayers;
  char *namesOfQuickPlayers;
  int numOfGames;
  int *numOfMovesPerGame;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.numOfAllPlayers;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.numOfQuickPlayers;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
  for (int i = 0; i < inputData.numOfQuickPlayers; i++) {
    iss >> inputData.namesOfQuickPlayers[i];
  }

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.numOfGames;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  inputData.numOfMovesPerGame = new int[inputData.numOfGames];
  for (int i = 0; i < inputData.numOfGames; i++) {
    iss >> inputData.numOfMovesPerGame[i];
  }
}

int main() {
    // freopen("input.txt","r",stdin);

  struct input_data inputData;
  process_stdin(inputData);

  solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
  return 0;
}