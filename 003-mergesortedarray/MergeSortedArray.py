# coding: utf-8
'''
leetcode-88
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
思路：最好从后往前进行排序
'''
def merge_sorted_array(L1, L2, m, n):
    if L2: #pop前要先判断L2是否为空
        l2 = L2.pop(-1)
    else:
        L1 = L1[:m+n]
        print(L1)
        return
    for i in range(m):
        while L1[m-(i+1)] < l2:
            L1.insert((m-i), l2)
            if L2:
                l2 = L2.pop(-1)
            else:
                L1 = L1[:m + n]
                print(L1)
                return
    if L2:
        L1 = L2 + L1
    L1 = L1[:m + n]
    print(L1)
    return


if __name__ =="__main__":
    L1 = [1,2,3]
    L2 = [2,5,6]
    merge_sorted_array(L1, L2, 3, 3)
