# align.py
# HW 11 Problem 2
# by Sidhant Rastogi
# for Python3


def align(str1, str2):
    if str1 == "":
        return [0, str2, "_" * len(str2)]
    if str2 == "":
        return [0, "_" * len(str1), str1]
    if str1[0] == str2[0]:
        l = align(str1[1:], str2[1:])
        return [1 + l[0], str1[0] + l[1], str2[0] + l[2]]
    else:
        l1 = align(str1, str2[1:])
        l2 = align(str1[1:], str2)

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

    ans = align(str1, str2)
    print(ans[0], ans[2], ans[1])

main()