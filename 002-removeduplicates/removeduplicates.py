# coding: utf-8
'''
leetcode:26
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
数组用元组表示，节省空间
'''
def remove_duplicates(l):
    if not l: # 若l为空，直接返回0
        return 0
    pre = l[0] # 初始化为第一个元素
    count = 1 # 初始化为1
    for i in enumerate(l[1:]): # 从第二个元素开始判断。若列表仅有一个元素，循环会被跳过
        if i != pre:
            l[count] = i
            count += 1
            pre = i


    return count


if __name__=="__main__":
    print(remove_duplicates([1,1,2]))
    print(remove_duplicates([1]))# 注意：若输出为元组且len为1, 12行会报错，因为一维元组会被视为int，不能切片。