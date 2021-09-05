//
// Created by Junho Kim on 2021/08/20.
//


#include <iostream>
#include <queue>
using namespace std;


struct Student {
    int id;
    int math, eng;
    Student(int num, int m, int e) : id(num), math(m), eng(e) {}    // 생성자 정의

    // 그냥 점수에 상관 없이 학번기준 학번이 작은것이 Top 을 유지 한다
    bool operator<(const Student s) const {
        return this->id > s.id;
    }
};

int main() {
    priority_queue<Student> pq;

    pq.push(Student(3, 100, 50));
    pq.push(Student(1, 60, 50));
    pq.push(Student(2, 80, 50));
    pq.push(Student(4, 90, 50));
    pq.push(Student(5, 70, 40));

// 학번을 기준으로 작은 것이 먼저 출력이 된다 그 이유는 구조체 내부의 연산자 오버로딩에 있다
    while (!pq.empty()) {
        Student ts = pq.top(); pq.pop();
        cout << "(학번, 수학 , 영어 ) : " << ts.id << ' ' << ts.math << ' ' << ts.eng << '\n';
    }

    priority_queue<int> p_qu_l;
    p_qu_l.push(1);
    p_qu_l.push(9);
    p_qu_l.push(5);
    int sz = p_qu_l.size();
    for(int i=0;i<sz;i++){
        cout << p_qu_l.top() << ',';
        p_qu_l.pop();
    }cout << '\n';

    priority_queue<int, vector<int>, greater<int>> p_qu_g;
    p_qu_g.push(1);
    p_qu_g.push(9);
    p_qu_g.push(5);
    sz = p_qu_g.size();
    for(int i=0;i<sz;i++){
        cout << p_qu_g.top() << ',';
        p_qu_g.pop();
    }cout << '\n';

    return 0;
}
