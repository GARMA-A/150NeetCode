from typing import List, Tuple


class TimeMap:
    def __init__(self):
        self.mp :dict[str , List[Tuple[str,int]]]= {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        res = ""
        values = self.mp[key]
        left , right = 0 , len(values)-1
        while left <= right:
            mid = left+(right-left) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid+1
            else:
                right = mid-1
        return res


