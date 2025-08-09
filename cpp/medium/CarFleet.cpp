#include <algorithm>
#include <csignal>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

class Solution {

public:
  int carFleet(int target, vector<int> &position, vector<int> &speed) {
    vector<pair<int, int>> cars;
    for (int i = 0; i < position.size(); i++) {
      cars.push_back({position[i], speed[i]});
    }
    sort(cars.begin(), cars.end(),
         [](const pair<int, int> &a, const pair<int, int> &b) {
           return a.first > b.first;
         });
    // after sorting them by position
    // if the time needed from the first car to reach the target
    // less than the car 2 then they will hit each other in some point
    //  time 1                  time 2
    //  2 sec for reach point > 100 sec for reach point
    //  speed = (dis / time) => time = (dis/speed)
    //  => dis=(target-pos)

    stack<double> st;

    for (int i = 0; i < cars.size(); i++) {

      double time = (double)(target - cars[i].first) / cars[i].second;
      if (st.empty() || time > st.top()) {
        st.push(time);
      }
    }
    return st.size();
  }
};

int main() {
  Solution *s1 = new Solution();
  vector<int> pos = {4, 1, 0, 7};
  vector<int> speed = {2, 2, 1, 1};
  s1->carFleet(10, pos, speed);
}
