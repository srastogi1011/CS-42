# FloydWarshall.py
# HW 10 Problem 2
# by Sidhant Rastogi
# for Python3

import math

infinity = math.inf

#graph1 = \
#    {"a": {"b": 3, "c": 7, "d": 5},
#     "b": {"a": 3, "c": 1, "e": 7},
#     "c": {"a": 7, "b": 1, "d": 3, "e": 2, "f": 3, "g": 2},
#     "d": {"a": 5, "c": 3, "f": 2},
#     "e": {"b": 7, "c": 2, "g": 2, "h": 1},
#     "f": {"c": 3, "d": 2, "g": 3, "i": 4},
#     "g": {"c": 2, "e": 2, "f": 3, "h": 3, "i": 2},
#     "h": {"e": 1, "g": 3, "i": 5},
#     "i": {"f": 4, "g": 2, "h": 5},
#     "j": {"k": 1},
#     "k": {"j": 1}}

def FloydWarshall(graph):
    nodes = list(graph.keys())
    dist = {dict1: {dict2: infinity for dict2 in nodes} for dict1 in nodes}

    for node1 in graph.keys():
        for node2 in graph[node1].keys():
            dist[node1][node2] = graph[node1][node2]

    for node1 in nodes:
        for node2 in nodes:
            if node1 == node2:
                dist[node1][node2] = 0

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def main():
    print(FloydWarshall(graph1))

main()