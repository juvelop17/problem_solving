//
// Created by Junho Kim on 2021/08/19.
//


// 메모리 공간 문제를 해결하기 위해 먼저 연결리스트 노드에 대한 메모리 풀을 다음과 같이 할당하겠습니다.
#define MAX_NODE 100
#define MAX_TREE 100

struct Node {
    int id = -1;
    Node *next = nullptr;
};

struct TreeNode {
    int parent = -1;
    Node *child = nullptr;
};

Node node[MAX_NODE];
int nodeCnt;

TreeNode treeNode[MAX_TREE];

int parent;
int child;
cin >> parent >> child;

treeNode[child].parent = parent;
Node *cur = &node[nodeCnt++];
cur->id = child;
cur->next = treeNode[parent].child->next;
treeNode[parent].child = cur;

// 부모 확인
int findRoot(int n) {
    while (treeNode[n].parent != -1)
        n = treeNode[n].parent;
    return n;
}

// 탐색
void traverse(int cur) {
    cout << cur << " ";
    for (ListNode* l = treeNode[cur].child; l != nullptr; l = l->prev)
        traverse(l->id);
}



///////

#define MAX_NODE 100
#define MAX_TREE 100

struct Node {
    int id = -1;
    Node *next = nullptr;
};

struct TreeNode {
    int parent = -1;
    Node *child = nullptr;
};

Node node[MAX_NODE];
int nodeCnt;

TreeNode treeNode[MAX_TREE];

int parent;
int child;
cin >> parent >> child;

treeNode[child].parent = parent;
Node *cur = &node[nodeCnt++];
cur->id = child;
cur->next = treeNode[parent].child->next;
treeNode[parent].child = cur;







