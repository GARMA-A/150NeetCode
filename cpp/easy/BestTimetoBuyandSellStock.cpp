#include <climits>
#include <vector>

using namespace std;

class Solution {
public:
  int maxProfit(vector<int> &prices) {

    int l = 0;
    int mx_profit = 0;
    for (int i = 1; i < prices.size(); i++) {
      if (prices[l] <= prices[i]) {
        mx_profit = max(mx_profit, prices[i] - prices[l]);

      } else {
        l = i;
      }
    }
    return mx_profit;
  }
};

int main() {}
