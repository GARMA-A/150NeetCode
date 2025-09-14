class Solution {
public:
  int getSum(int a, int b) {
    int res = 0;
    int carry = 0;
    for (int i = 0; i < 32; i++) {
      int first_bit = (a & 1), second_bit = (b & 1);
      int current_bit = carry ^ first_bit ^ second_bit;
      carry =
          (first_bit & second_bit) | (first_bit & carry) | (second_bit & carry);
      res |= (current_bit << i);
      first_bit >>= 1;
      second_bit >>= 1;
    }
    return res;
  }
};
