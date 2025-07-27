#include <iostream>
#include <iterator>
#include <list>
#include <queue>
#include <stack>
#include <unordered_map>
#include <variant>
#include <vector>

using namespace std;

class Graph {
  vector<vector<int>> adjMatrix;

public:
  Graph(int numberOfNodes) {
    adjMatrix.resize(numberOfNodes, vector<int>(numberOfNodes, 0));
  }
  int addVertex() {
    int newSize = adjMatrix.size() + 1;
    for (auto &row : adjMatrix) {
      row.resize(newSize, 0);
    }
    adjMatrix.push_back(vector<int>(newSize, 0));
    return adjMatrix.size();
  }

  bool addEdge(int from, int to) {
    if (from >= adjMatrix.size() || to >= adjMatrix.size() || from < 0 ||
        to < 0) {
      return false;
    }
    adjMatrix[from][to] = 1;
    return true;
  }

  void printGraph() {
    for (int i = 0; i < adjMatrix.size(); i++) {
      cout << i << " -> ";
      for (int j = 0; j < adjMatrix[i].size(); j++) {
        if (adjMatrix[i][j] == 1) {
          cout << j << " ";
        }
      }
      cout << endl;
    }
  }

  void DFS(int from = 0) {
    vector<bool> visited(adjMatrix.size(), false);
    stack<int> s;
    s.push(from);
    while (not s.empty()) {
      int current = s.top();
      s.pop();
      if (not visited[current]) {
        visited[current] = true;
        cout << current << " ";
        for (int i = 0; i < adjMatrix[current].size(); i++) {
          if (adjMatrix[current][i] == 1 and !visited[i]) {
            s.push(i);
          }
        }
      }
    }
  }
  void r_DFS(int from, vector<bool> &visited) {
    if (visited[from]) {
      return;
    }
    visited[from] = true;
    cout << from << " ";
    for (int i = 0; i < adjMatrix.size(); i++) {
      if (adjMatrix[from][i] == 1 and not visited[i]) {
        r_DFS(i, visited);
      }
    }
  }

  void BFS(int from = 0) {
    vector<bool> visited(adjMatrix.size(), false);
    queue<int> q;
    q.push(from);
    while (not q.empty()) {
      int current = q.front();
      q.pop();
      if (not visited[current]) {
        cout << current << " ";
        visited[current] = true;
        for (int i = 0; i < adjMatrix.size(); i++) {
          if (not visited[i] and adjMatrix[current][i] == 1) {
            q.push(i);
          }
        }
      }
    }
  }
};

class Graph2 {

  vector<list<char>> adjList;

public:
  Graph2(int numberOfNodes) { adjList.resize(numberOfNodes); }
  int addVertex() {
    adjList.push_back(list<char>());
    return adjList.size();
  }

  bool addEdge(int from, char to) {
    if (from >= adjList.size() || from < 0) {
      return false;
    }
    adjList[from].push_back(to);
    return true;
  }

  void printGraph() {
    for (int i = 0; i < adjList.size(); i++) {
      cout << i << " -> ";
      for (char node : adjList[i]) {
        cout << node << " ";
      }
      cout << endl;
    }
  }

  void DFS(int from) {
    vector<bool> visited(adjList.size(), false);
    stack<int> s;
    s.push(from);
    while (!s.empty()) {
      int current = s.top();
      s.pop();
      if (!visited[current]) {
        visited[current] = true;
        cout << current << " ";
        for (auto it = adjList[current].rbegin(); it != adjList[current].rend();
             ++it) {
          int neighbor = *it - 'A'; // Assuming nodes are labeled 'A', 'B', etc.
          if (neighbor >= 0 && neighbor < adjList.size() &&
              !visited[neighbor]) {
            s.push(neighbor);
          }
        }
      }
    }
  }

  // implement for me DFS function iterative version
};

int main() {
  // Graph g = Graph(7);
  // g.addEdge(0, 1);
  // g.addEdge(0, 2);
  // g.addEdge(1, 3);
  // g.addEdge(1, 4);
  // g.addEdge(2, 5);
  // g.addEdge(2, 6);
  // g.DFS(0);
  // vector<bool> visited(7, false);
  // cout << endl;
  // g.r_DFS(0, visited);
  // cout << endl;
  // g.BFS(0);
  // ----------------------------
  Graph2 g2(5);
  g2.addEdge(0, 'A');
  g2.addEdge(0, 'B');
  g2.addEdge(1, 'C');
  g2.addEdge(1, 'D');
  g2.addEdge(2, 'E');
  g2.addEdge(3, 'F');
  g2.addEdge(4, 'G');
  g2.printGraph();
  cout << endl;
  g2.DFS(0);
}
