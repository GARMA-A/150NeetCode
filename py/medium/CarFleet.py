from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position,speed) , key=lambda x:-x[0])
        st = [float(-1)]
        for pos , spd in pos_speed:
            cur_time = (target-pos) / spd
            if st[-1] < cur_time:
                st.append(cur_time)
        return len(st)-1

