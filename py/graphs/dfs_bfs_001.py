from typing import List, Mapping, Set, Deque
from collections import deque


adj_list = {}
adj_list["a"] = ["b", "c"]
adj_list["b"] = ["e", "f"]
adj_list["c"] = ["d"]
adj_list["d"] = []
adj_list["e"] = []
adj_list["f"] = []


def DFS(mp: Mapping[str, List[str]], startNode: str, visited: Set[str]):
    print("visited : ", startNode, end="\n")
    visited.add(startNode)
    for s in mp[startNode]:
        DFS(mp, s, visited)


# DFS(adj_list, "a", set())
# print("=================", end="\n")


def DFS_Itr(mp: Mapping[str, List[str]], startNode: str, visited: Set[str]):
    stack = [startNode]
    while stack:
        top = stack.pop()
        print("visited :", top, end="\n")
        for el in mp[top]:
            if el not in visited:
                visited.add(el)
                stack.append(el)


# DFS_Itr(adj_list, "a", set())


def BFS(
    mp: Mapping[str, List[str]], startNode: str, visited: Set[str], queue: Deque[str]
):
    queue.append(startNode)
    while len(queue):
        top = queue.popleft()
        visited.add(top)
        print("visited :", top, end="\n")
        for s in mp[top]:
            if s not in visited:
                queue.append(s)


# BFS(adj_list, "a", set(), deque())

array_list: List[List[str]] = [
    ["0", "1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "1", "1"],
    ["0", "0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
]


def DFS2(arr: List[List[str]], startRow: int, visited: Set[int]):
    print("visited", startRow, end="\n")
    visited.add(startRow)
    for idx in range(len(arr[startRow])):
        if arr[startRow][idx] == "1":
            DFS2(arr, idx, visited)


def DFS2_Itr(arr: List[List[str]], startRow: int, visited: Set[int]):
    stack = [startRow]
    while stack:
        top = stack.pop()
        print("vistied :", chr(top + 97), end="\n")
        for i, el in enumerate(arr[top]):
            if el == "1" and el not in visited:
                visited.add(i)
                stack.append(i)


# DFS2_Itr(array_list, 0, set())


def BFS2(arr: List[List[str]], startNode: int, visited: Set[int], queue: Deque[int]):
    queue.append(startNode)
    while len(queue):
        top = queue.popleft()
        visited.add(top)
        print("visited : ", top, end="\n")
        for idx in range(len(arr[top])):
            if idx not in visited:
                visited.add(idx)
                queue.append(idx)


# BFS2(array_list, 0, set(), deque())
# DFS2(array_list, 0, set())
