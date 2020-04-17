import sys
import time

N: int = int()
M: int = int()
GRAPH: dict = dict()
VISITED: set = set()

def DFS(node: int):
    global GRAPH, VISITED
    if node not in VISITED:
        print(node)
        VISITED.add(node)
        for neighbour in GRAPH[node]:
            DFS(neighbour)

def hashPathDFS(source: int, destination: int):
    global N, M, GRAPH, VISITED
    if source in VISITED:
        return False
    VISITED.add(source)
    if source == destination:
        return True
    for i in GRAPH[source]:
        if hashPathDFS(i, destination):
            return True
    return False

def main():
    global N, M, GRAPH
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    for i in range(N):
        GRAPH[i] = tuple(map(int, sys.stdin.readline().split()))

    for i in range(N):
        print(*GRAPH[i])
    print('------------')

    x, y = 4, 1
    print(hashPathDFS(x - 1, y - 1))

if __name__ == '__main__':
    HELLO_WORLD = True
    if HELLO_WORLD is True:
        sys.stdin = open('graph.in.txt', 'r')
        start_time = time.time()
        main()
        print("--- %.5s seconds ---" % (time.time() - start_time))
    else:
        main()
