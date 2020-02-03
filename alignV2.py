# alignV2.py
# HW 11 Problem 3
# by Sidhant Rastogi
# for Python3


from copy import deepcopy


def align(str1, str2, table):
    if str1 == "":
        table[str1][str2] = [0, str2, "_" * len(str2)]
        return table[str1][str2]
    if str2 == "":
        table[str1][str2] = [0, "_" * len(str1), str1]
        return table[str1][str2]
    if str1[0] == str2[0]:
        if table[str1[1:]][str2[1:]] is not None:
            l = deepcopy(table[str1[1:]][str2[1:]])
        else:
            table[str1[1:]][str2[1:]] = align(str1[1:], str2[1:], table)
            l = deepcopy(table[str1[1:]][str2[1:]])
        return [1 + l[0], str1[0] + l[1], str2[0] + l[2]]
    else:
        if table[str1][str2[1:]] is not None:
            l1 = deepcopy(table[str1][str2[1:]])
        else:
            table[str1][str2[1:]] = align(str1, str2[1:], table)
            l1 = deepcopy(table[str1][str2[1:]])

        if table[str1[1:]][str2] is not None:
            l2 = deepcopy(table[str1[1:]][str2])
        else:
            table[str1[1:]][str2] = align(str1[1:], str2, table)
            l2 = deepcopy(table[str1[1:]][str2])

        if l1[0] > l2[0]:
            l1[1] = str2[0] + l1[1]
            l1[2] = "_" + l1[2]
            return [l1[0], l1[1], l1[2]]
        else:
            l2[1] = "_" + l2[1]
            l2[2] = str1[0] + l2[2]
            return [l2[0], l2[1], l2[2]]


def main():
    str1 = "GTACGTCGATAACTG"
    str2 = "TGATCGTCATAACGT"
    table = {}
    for i in range(0, len(str1) + 1):
        sub = {}
        for j in range(0, len(str2) + 1):
            sub[str2[j:]] = None
        table[str1[i:]] = sub

    ans = align(str1, str2, table)
    print(ans[0], ans[2], ans[1])


main()