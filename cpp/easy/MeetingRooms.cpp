#include <algorithm>
#include <ios>
#include <iostream>
#include <vector>
using namespace std;

class Interval {
public:
  int start, end;
  Interval(int start, int end) {
    this->start = start;
    this->end = end;
  }
};

class Solution {
public:
  bool canAttendMeetings(vector<Interval> &intervals) {
    if (intervals.empty())
      return true;
    sort(
        intervals.begin(), intervals.end(),
        [](const Interval &a, const Interval &b) { return a.start < b.start; });

    Interval past = intervals[0];

    for (int i = 1; i < intervals.size(); i++) {
      if (past.end > intervals[i].start) {
        return false;
      }
      past = intervals[i];
    }

    return true;
  }
};
