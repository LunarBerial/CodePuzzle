#coding: utf-8
'''
leetcode: 165
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
思路：给出的是一个已排好序的list。因此最快的方法就是设置前后两个指针。使其元素相加，大于目标则尾指针前移，小于则头指针后移
'''
def twosum(l:list, target: int):
    f = 0
    p = len(l) - 1

    while l[f] + l[p] != target and f < p:
        if l[f] + l[p] > target:
            p -= 1
        elif l[f] + l[p] < target:
            f += 1

    if l[f] + l[p] == target:
        return f, p
    else:
        return None, None


if __name__=="__main__":
    print(twosum([2, 7, 11, 15], 9))