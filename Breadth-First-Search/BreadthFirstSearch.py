from collections import deque
from typing import List, Dict

def BFS(GRAPH: Dict[str, List[str]], vertex: str):
    QUEUE: deque = deque([])
    VISITED: set = set()
    QUEUE.append(vertex)
    while QUEUE:
        P: str = QUEUE.popleft()
        VISITED.add(P)
        print(P, end=" ")
        for i in GRAPH[P]:
            if i not in VISITED:
                QUEUE.append(i)
                VISITED.add(i)
    print()

def main():
    GRAPH: Dict[str, List[str]] = {
        "0": ["1", "2"],
        "1": ["0", "3", "4"],
        "2": ["0", "4", "5"],
        "3": ["1", "6"],
        "4": ["1", "2", "6", "7"],
        "5": ["2", "7"],
        "6": ["3", "4", "8"],
        "7": ["4", "5", "8"],
        "8": ["6", "7"],
    }
    BFS(GRAPH, "0")

if __name__ == "__main__":
    main()
