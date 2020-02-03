# llcs.py
# HW 11 Problem 1
# by Sidhant Rastogi
# for Python3


def llcs(str1, str2):
    if str1 == "" or str2 == "":
        return 0
    if str1[0] == str2[0]:
        return 1 + llcs(str1[1:], str2[1:])
    else:
        return max(llcs(str1, str2[1:]), llcs(str1[1:], str2))


def main():
    print(llcs("GTACGTCGATAACTG", "TGATCGTCATAACGT"))


main()