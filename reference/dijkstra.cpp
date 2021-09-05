//
// Created by Junho Kim on 2021/08/19.
//


struct Edge {
    int start, end, cost;
    Edge *next;

    bool operator<(const Edge e) const {
        return this->cost > e.cost;
    }
};

struct Room {
    Edge *edges = nullptr;
};

Edge edge[MAX_M], rev_edge[MAX_M];
int edge_cnt;

void dijkstra(Room _room[], int X, int costs[]) {
    priority_queue<Edge> pq;

    pq.push({X, X, 0, nullptr});
    costs[X] = 0;
    while (!pq.empty()){
        Edge cur_node = pq.top();
        pq.pop();

        if (costs[cur_node.end] < cur_node.cost) {
            continue;
        }

        Edge *next_node = _room[cur_node.end].edges;
        while (next_node != nullptr) {
            if (costs[next_node->end] > cur_node.cost + next_node->cost) {
                costs[next_node->end] = cur_node.cost + next_node->cost;
                pq.push({cur_node.start, next_node->end, cur_node.cost + next_node->cost, nullptr});
            }
            next_node = next_node->next;
        }
    }
}
