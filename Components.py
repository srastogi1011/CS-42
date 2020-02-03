# Components.py
# HW 10 Problem 1
# by Sidhant Rastogi
# for Python3

#graph1 = \
#    {"a": {"b": 3, "c": 7, "d": 5},
#     "b": {"a": 3, "c": 1, "e": 7},
#     "c": {"a": 7, "b": 1, "d": 3, "e": 2, "f": 3, "g": 2},
#     "d": {"a": 5, "c": 3, "f": 2},
#     "e": {"b": 7, "c": 2, "g": 2, "h": 1},
#     "f": {"c": 3, "d": 2, "g": 3, "i": 4},
#     "g": {"c": 2, "e": 2, "f": 3, "h": 3, "i": 2},
#     "h": {"e": 1, "g": 3, "i": 5},
#     "i": {"f": 4, "g": 2, "h": 5}}

def components(graph):
    comps = {}
    num = 0
    for node in graph.keys():
        if node in comps:
            continue
        v = comps.setdefault(node, num)
        for k in graph[node].keys():
            v = comps.setdefault(k, num)
        num += 1
    return comps

def main():
    print(components(graph1))

main()