#coding: utf-8
'''
leetcode 219

给定一个列表l和整数k，若列表中存在两个相同的数且距离不大于k, 则返回True， 否则返回False

用dictionary辅助解决，实时更新数字和索引的信息
'''
def containnums(vector: list, k: int):
    d = {}
    for idx, num in enumerate(vector):
        if num in d and idx - d[num] <= k:
            return True
        d[num] = idx

    return False


if __name__=="__main__":
    print(containnums([1, 2, 3, 1], 3))