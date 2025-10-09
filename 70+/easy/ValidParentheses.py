class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1 :
            return False

        st = []
        for ch in s:
            if ch == "[" or ch == "{" or ch == "(":
                st.append(ch)
                continue
            if  ((ch == ")" and st   and st[-1] == "(")
                        or (ch=="}" and st and st[-1]=="{")
                        or (ch=="]" and st and st[-1] == "[")
                       ):
                    st.pop()
                    continue

            return False


        return not st


