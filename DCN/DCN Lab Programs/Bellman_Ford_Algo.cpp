/*
1. This algo can be used for -ve weights in D and UnD Graphs as well
2. Cannot be used in negative cycle
3. But can be used for -ve cycle detection 
*/
#include <bits/stdc++.h>
using namespace std;

vector<int> bellmanFord(int n, int m, int src, vector<vector<int>>& edges) {
    vector<int> dist(n, INT_MAX); // Initialize distances to infinity
    dist[src] = 0; // Distance to source vertex is 0

    // Relax edges for n-1 iterations
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < m; ++j) {
            int u = edges[j][0];
            int v = edges[j][1];
            int weight = edges[j][2];
            if (dist[u] != INT_MAX && dist[v] > dist[u] + weight) {
                dist[v] = dist[u] + weight;
            }
        }
    }

    // Check for negative cycles
    bool flag = false;
    for (int j = 0; j < m; ++j) {
        int u = edges[j][0];
        int v = edges[j][1];
        int weight = edges[j][2];
        if (dist[u] != INT_MAX && dist[v] > dist[u] + weight) {
            flag = true; // Negative cycle detected
        }
    }

    // Optionally handle negative cycle detection
    // if (flag) {
    //     return {0}; // Negative cycle exists
    // }

    return dist;
}

int main() {
    int n = 5; // Number of vertices
    int m = 7; // Number of edges

    // Example edges vector
    vector<vector<int>> edges = {
        {0, 1, -1}, // Edge from vertex 0 to vertex 1 with weight -1
        {0, 2, 4},  // Edge from vertex 0 to vertex 2 with weight 4
        {1, 2, 3},  // Edge from vertex 1 to vertex 2 with weight 3
        {1, 3, 2},  // Edge from vertex 1 to vertex 3 with weight 2
        {1, 4, 2},  // Edge from vertex 1 to vertex 4 with weight 2
        {3, 2, 5},  // Edge from vertex 3 to vertex 2 with weight 5
        {3, 1, 1}   // Edge from vertex 3 to vertex 1 with weight 1
    };

    int src = 0; // Source vertex for Bellman-Ford algorithm

    vector<int> shortestDistances = bellmanFord(n, m, src, edges);

    // Output the shortest distances from the source vertex
    for (int i = 0; i < n; ++i) {
        cout << "Distance to vertex " << i << " from source: ";
        if (shortestDistances[i] == INT_MAX) {
            cout << "INF" << endl;
        } else {
            cout << shortestDistances[i] << endl;
        }
    }

    return 0;
}