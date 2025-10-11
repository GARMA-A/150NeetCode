from typing import List


def find_max_and_second_max(nums: List[int]):
    mx, sec_mx= float("-inf"), float("-inf")

    for num in nums:
        old = mx
        mx = max(mx, num)
        if old != mx:
            sec_mx = old
    return [mx, sec_mx]


print(find_max_and_second_max([1, 4, 5, 2, 9]))
