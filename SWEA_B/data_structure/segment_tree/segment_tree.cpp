#include <iostream>
#include <vector>

using namespace std;


vector<int> tree;
vector<int> arr;


int init(int node, int start, int end) {
    if(start == end) {
        tree[node] = arr[start];
        return tree[node];
    }
    tree[node] = init(node*2,start,(start+end)/2)
        + init(node*2+1,(start+end)/2+1,end);
    return tree[node];
}


int sum(int node, int start, int end, int left, int right) {
    if (right < start || left > end) {
        return 0;
    }
    if (left <= start && right >= end) {
        return tree[node];
    }
    return sum(node*2,start,(start+end)/2,left,right)
         + sum(node*2+1,(start+end)/2+1,end,left,right);
}


void update(int node, int start, int end, int index, int diff) {
    if (index < start || index > end) {
        return;
    }
    tree[node] += diff;
    if (start != end) {
        update(node*2, start, (start+end)/2, index, diff);
        update(node*2, (start+end)/2 + 1, end, index, diff);
    }
}


int main() {
    
}


