#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
  int directions[4][2] = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};

public:
  int numIslands(vector<vector<char>> &grid) {
    int ROWS = grid.size(), COLUM = grid[0].size();
    int numOfIslands = 0;
    for (int r = 0; r < ROWS; r++) {

      for (int c = 0; c < COLUM; c++) {
        if (grid[r][c] == '1') {
          DFS(grid, r, c);
          numOfIslands++;
        }
      }
    }
    return numOfIslands;
  }

  void DFS(vector<vector<char>> &grid, int r, int c) {
    if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() ||
        grid[r][c] == '0') {
      return;
    }

    grid[r][c] = '0';
    for (int i = 0; i < 4; i++) {
      DFS(grid, r + directions[i][0], c + directions[i][1]);
    }
  }
};

int main() {}
