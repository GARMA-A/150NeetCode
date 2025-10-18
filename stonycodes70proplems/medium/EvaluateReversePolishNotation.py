from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for s in tokens:
            if s not in {"+" , "-" , "/" , "*"}:
                st.append(s)
            else:
                second = int(st.pop())
                first = int(st.pop())
                if s=="+":
                    st.append(first+second)
                elif s=="-":
                    st.append(first-second)
                elif s=="*":
                    st.append(first*second)
                else:
                    st.append(int(first/second))


        return int(st.pop()) if st else 0


