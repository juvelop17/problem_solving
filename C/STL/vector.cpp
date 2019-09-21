#include <iostream>
#include <vector>
using namespace std;

struct Node {
	int a;
};

int n = 5, m = 5;

template <class T>
void monitor_vector(vector<T> vec) {
	cout << "monitor_vector" << endl;
	cout << "vec.size() " << vec.size() << endl;

	for (int i = 0; i < vec.size(); i++) {
		cout << vec.at(i) << " ";
	}
	cout << endl;
}

template <class T>
void monitor_matrix_vector(vector<T> vec) {
	cout << "monitor_matrix_vector" << endl;

	for (int i = 0; i < vec.size(); i++) {
		for (int j = 0; j < vec.size(); j++) {
			cout << vec.at(i).at(j) << " ";
		}
		cout << endl;
	}
	cout << endl;
}



int main() {
	cout << "start program\n";
	printf("%d %d\n", n, m);

	vector<int> vec1;
	vector<double> vec2;

	// 사용자가 정의한 Node 구조체를 저장
	vector<Node> vec3;

	// 벡터의 초기 크기를 n으로 설정
	vector<int> vec4(n);

	// 벡터의 초기 크기를 n으로 설정하고 1로 초기화
	vector<int> vec5(n, 1);

	// 크기가 n*m인 2차원 벡터를 선언하고 0으로 초기화
	vector<vector<int>> vec6(n, vector<int>(m, 0));

	// 벡터의 맨 뒤에 원소 5 추가
	vec1.push_back(5);

	// 벡터의 맨 뒤 원소 삭제
	vec1.pop_back();

	// 벡터의 크기 출력
	printf("vector size : %d\n", vec1.size());

	// 벡터의 크기를 n으로 재설정
	vec1.resize(3);

	// 벡터의 모든 원소 삭제
	vec1.clear();

	//벡터의 첫 원소의 주소, 마지막 원소의 다음 주소 리턴
	//printf("vec1.begin() : %X\n", vec1.begin());
	//printf("vec1.end() : %X\n", vec1.end());
	//cout << "vec1.begin() : " << vec1.begin();
	//cout << "vec1.end() : " << vec1.end();

	////[a, b) 주소 구간에 해당하는 원소 삭제
	//vec1.erase(vec1.begin(), vec1.end());//모든 원소 삭제

	//									 //vec7은 vec1의 2번째 원소부터 마지막 원소까지 복사하여 생성
	//vector<int> vec7 = vector<int>(vec1.begin() + 2, vec1.end());




	 vector<char> _vec1(5, 'a');
	 monitor_vector(_vec1);

	 _vec1.clear();
	 monitor_vector(_vec1);

	 _vec1.push_back('b');
	 monitor_vector(_vec1);

	 _vec1.insert(_vec1.begin(), 'c');
	 _vec1.insert(_vec1.begin(), 'c');
	 monitor_vector(_vec1);

	 _vec1.insert(_vec1.begin()+1, 'd');
	 _vec1.insert(_vec1.begin()+2, 'e');
	 monitor_vector(_vec1);

	 vector<vector<int>> _vec2(5, vector<int>(5, 10));
	 monitor_matrix_vector(_vec2);


	return 0;
}

