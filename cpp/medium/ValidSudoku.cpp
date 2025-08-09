#include <iostream>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  bool isValidRow(vector<vector<char>> &board) {
    for (int i = 0; i < 9; i++) {
      unordered_set<char> st;
      for (int j = 0; j < 9; j++) {
        if (board[i][j] == '.')
          continue;
        int size = st.size();
        st.insert(board[i][j]);
        if (st.size() == size)
          return false;
      }
    }
    return true;
  }

  bool isValidColumn(vector<vector<char>> &board) {

    for (int i = 0; i < 9; i++) {
      unordered_set<char> st;
      for (int j = 0; j < 9; j++) {

        if (board[j][i] == '.')
          continue;
        int size = st.size();
        st.insert(board[j][i]);
        if (st.size() == size)
          return false;
      }
    }
    return true;
  }
  bool isValidSquare(vector<vector<char>> &board) {
    vector<pair<int, int>> points = {{0, 0}, {0, 3}, {0, 6}, {3, 0}, {3, 3},
                                     {3, 6}, {6, 0}, {6, 3}, {6, 6}};
    for (int curp = 0; curp < 9; curp++) {

      unordered_set<char> st;
      for (int i = points[curp].first; i < (points[curp].first + 3); i++) {
        for (int j = points[curp].second; j < (points[curp].second + 3); j++) {

          if (board[i][j] == '.')
            continue;
          int size = st.size();
          st.insert(board[i][j]);
          if (st.size() == size)
            return false;
        }
      }
    }
    return true;
  }

  bool isValidSudoku(vector<vector<char>> &board) {

    return this->isValidRow(board) and this->isValidColumn(board) and
           this->isValidSquare(board);
  }
};

int main() {}
