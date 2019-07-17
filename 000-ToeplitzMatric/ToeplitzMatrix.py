# coding: utf-8
import numpy as np

'''
托普利兹矩阵：任意斜对角线的元素相等，矩阵不一定为方阵（mxn）
reference：https://www.cnblogs.com/grandyang/p/8729459.html
思路：1. 按照每条斜对角线一一检查。但需要单独构造（m+n-1-2（因为左下，右上对角线元素个数为1，不需要检查））对角线，添加条件，比较麻烦。
    2. 遍历矩阵元素，若发现其右下位元素与之不等，即返回。
'''


def IsToeplizeMatric(m):
    assert len(m.shape) == 2, "matrix needs to be 2-dimensions"

    flag = True
    for i in range(m.shape[0] - 1):
        for j in range(m.shape[1] - 1):
            if not m[i, j] == m[i + 1, j + 1]:
                flag = False
                return flag
    return flag


if __name__ == "__main__":
    m = np.array([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
    print(IsToeplizeMatric(m))

    m = np.array([[1, 2], [2, 2]])
    print(IsToeplizeMatric(m))
