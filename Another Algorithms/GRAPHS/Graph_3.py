graph = {
    "Misha" : ["Dima", "Sasha", "Mike"],
    "Sasha" : ["Mike", "Misha"],
    "Mike" : ["Sasha", "Misha"],
    "Dima" : ["Misha"]
}

# def all_friends(graph):
#     print(graph["Misha"])
#     print(graph["Sasha"])
#     print(graph["Mike"])
#     print(graph["Dima"])
#
# all_friends(graph)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end=" ")

    for friend in graph[start]:
        if friend not in visited:
            dfs(graph, friend, visited)

dfs(graph, "Misha", visited=None) # -> Misha Dima Sasha Mike