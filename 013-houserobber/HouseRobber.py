#coding: utf-8
'''
leetcode: 198 https://leetcode.com/problems/house-robber/description/
解：动态规划问题。打劫相邻的两栋会触发警报，保证打劫的财产最多。
'''
def houserobber(n:list):
    if not n:
        return 0
    if len(n) == 1:
        return n[0]

    pre = n[0]
    cur = max(pre, n[1])
    for i in range(2, len(n)):
        cur, pre = max(pre + n[i], cur), cur
    return cur


if __name__=="__main__":
    print(houserobber([1, 3, 5, 2, 4, 6]))
