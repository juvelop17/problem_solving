
#include <iostream>


#define MAX_REQ 100000

struct TreeNode {
    int value = -1;
    TreeNode *left = nullptr;
    TreeNode *right = nullptr;
};

struct Tree {
    TreeNode *root = nullptr;
};


Tree *tree;
TreeNode treeNode[MAX_REQ];
int treeNodeCnt;


void init(){
    tree = new Tree();
    treeNodeCnt = 0;
}

TreeNode *nodeSearch(int value) {
    TreeNode *cur = tree->root;
    while (cur != nullptr && cur->value != value) {
        if (cur->value > value) {
            cur = cur->left;
        } else {
            cur = cur->right;
        }
    }
    return cur;
}

void nodeInsert(int value) {
    TreeNode *cur = tree->root;
    TreeNode *parent = nullptr;
    treeNode[treeNodeCnt] = {value, nullptr, nullptr};

    while (cur) {
        parent = cur;
        if (cur->value > value) {
            cur = cur->left;
        } else {
            cur = cur->right;
        }
    }

    if (parent == nullptr) {
        tree->root = &treeNode[treeNodeCnt++];
    } else {
        if (parent->value > value){
            parent->left = &treeNode[treeNodeCnt++];
        } else {
            parent->right = &treeNode[treeNodeCnt++];
        }
    }
}

int nodeRemove(int value) {
    TreeNode *cur = tree->root;
    TreeNode *parent = nullptr;
    while (cur && cur->value != value) {
        parent = cur;
        cur = cur->value < value ? cur->right : cur->left;
    }

    if (!cur) {
        return -1;
    }

    // child 0
    if (cur->left && cur->right) {
        if (parent) {
            if (parent->left == cur) {
                parent->left = nullptr;
            }
            else {
                parent->right = nullptr;
            }
        }
        else {
            tree->root = nullptr;
        }
    }

    // child 1
    else if (cur->right == nullptr || cur->left == nullptr) {
        TreeNode *child = cur->left ? cur->left :cur->right;
        if (parent) {
            if (parent->left == cur) {
                parent->left = child;
            }
            else {
                parent->right = child;
            }
        }
        else {
            tree->root = child;
        }
    }

    // child 2
    else {
        TreeNode *successor = cur->right;
        TreeNode *successorParent = nullptr;

        while (successor->left) {
            successorParent = successor;
            successor = successor->left;
        }

        if (successor->right) {
            successorParent->left = successor->right;
        }
        else {
            successorParent->left = nullptr;
        }
        cur->value = successor->value;
    }
}

//void nodeSide(int value, TreeNode *predecessor, TreeNode *successor) {
//    TreeNode *cur = tree->root;
//
//    while (cur && cur->value != value) {
//        if (cur->value < value) {
//            predecessor = cur;
//            cur = cur->right;
//        }
//        else {
//            successor = cur;
//            cur = cur->left;
//        }
//    }
//    if (cur->left) {
//
//    }
//}

int main() {
    init();

    nodeInsert(1);
    nodeInsert(2);
    nodeInsert(3);
    nodeInsert(4);
    nodeInsert(5);
    nodeInsert(6);

//    printf("%d %d\n", 1, nodeSearch(1));
//    printf("%d %d\n", 2, nodeSearch(2));
//    printf("%d %d\n", 2, nodeSearch(2));
//    nodeRemove(2);
//    printf("%d %d\n", 2, nodeSearch(2));

    return 0;
}