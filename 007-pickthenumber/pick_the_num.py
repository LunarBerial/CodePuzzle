#coding: utf-8

'''
LeetCode：136
注意：题目要求找出数组中只存在一次的数字。
这里利用了异或的性质。
a^a = 0, a^a^b = b
这样连续异或，最后得到的数字就是只出现一次的数。
又PS：这里不用特意将数字转成二进制。
'''
def pick_the_num(num):
    t_num = 0
    for i in num:
        t_num ^= i

    return t_num