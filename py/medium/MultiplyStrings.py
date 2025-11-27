
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans ="" 
        final_sum = 0
        for digit1 in num1:
            num_digit1 = ord(digit1) - ord("0")
            sum = 0
            digit_place = len(num2) 
            for digit2 in num2:
                num_digit2 = ord(digit2) - ord("0")
                sum +=  num_digit1 * num_digit2
            final_sum += sum

        while final_sum:
            digit = final_sum % 10
            ans+=str(digit)
            final_sum //= 10
        final_ans =""
        for idx in range(len(ans)-1 , -1 , -1):
           final_ans += ans[idx]

        return str(int(num1) * int(num2))








