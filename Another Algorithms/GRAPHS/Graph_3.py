from collections import deque

graph = {
    "Misha" : ["Dima", "Sasha", "Mike"],
    "Sasha" : ["Mike", "Misha"],
    "Mike" : ["Sasha", "Misha"],
    "Dima" : ["Misha"]
}

def all_friends(graph):
    print(graph["Misha"])
    print(graph["Sasha"])
    print(graph["Mike"])
    print(graph["Dima"])

all_friends(graph)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end=" ")

    for friend in graph[start]:
        if friend not in visited:
            dfs(graph, friend, visited)

dfs(graph, "Misha", visited=None) # -> Misha Dima Sasha Mike

def bfs(graph, start):
    visited = set()
    queue = deque([start]) # queue - очередь

    while queue:
        vertex = queue.popleft() # vertex - вершина
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex])

bfs(graph, "Misha")