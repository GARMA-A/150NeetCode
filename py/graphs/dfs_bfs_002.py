from collections import deque
from enum import verify
from typing import List, Mapping

adj_list : Mapping[str , List[str] ]= {}
adj_list["A"] = ["B" ,"C"]
adj_list["B"] = ["A","D"]
adj_list["C"]  = []
adj_list["D"] = ["F"]
adj_list["E"] = []
adj_list["F"] = ["E"]

def DFS(startNode:str):
    stack = [startNode]
    visited = {}
    while stack:
        top = stack.pop()
        print(top , end=" ")
        visited[top] = True
        for node in adj_list[top]:
            if node not in visited:
                visited[node] = True
                stack.append(node)

def rec_DFS(startNode:str , visited = {}):
    if visited.get(startNode , False):
        return
    print(startNode , end=" ")
    visited[startNode] = True
    for neighbor in adj_list[startNode]:
        rec_DFS(neighbor , visited)

DFS("A")
print()
rec_DFS("A")
# print()

def BFS(startNode:str):
    q = deque(startNode)
    visited = {}
    while q:
        top = q.popleft()
        visited[top] =True
        print(top , end=" ")
        for node in adj_list[top]:
            if node not in visited:
                visited[node] = True
                q.append(node)
#BFS("A")

# A B C D E F
twoDArray =[
[0, 1, 1, 0, 0, 0],
[1, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0]
 ]



def DFS2(startNode : str):
    stack = [startNode]
    visited = set()
    while stack:
        top= stack.pop()
        visited.add(top)
        print(top ,end=" ")
        for idx,val in enumerate(twoDArray[ord(top)-ord("A")]):
            ch = chr(ord("A") + idx)
            if val and ch not in visited:
                visited.add(str(ord("A")+idx))
                stack.append(ch)
print()
# DFS2("A")




def BFS2(startNode :str):
    q = deque(startNode)
    visited = set()
    while q:
        top = q.popleft()
        visited.add(top)
        print(top ,  end=" ")
        for idx ,val in enumerate(twoDArray[ord(top)-ord("A")]):
            ch = chr(ord("A")+idx)
            if val and ch not in visited:
                visited.add(ch)
                q.append(ch)

#BFS2("A")







