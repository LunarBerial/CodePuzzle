#coding: utf-8
'''
leetcode : 191: https://leetcode-cn.com/problems/number-of-1-bits/solution/wei-1de-ge-shu-by-leetcode/
描述：给一个十进制的数，返回其二进制表示中1的个数
'''

#法一：不断与（N-1）做按位与，每做一次会消掉一个末尾的1.
def NumbersofOneinBits(n:int):
    count = 0
    while n:
        count += 1
        n = n & (n -1)
    return count


#法二：转成二进制后遍历
def NumbersofOneinBits_2(n:int):
    count = 0
    n = bin(n)
    for i in n[2:]:
        if i == '1':
            count += 1
    return count

if __name__=="__main__":
    c = NumbersofOneinBits_2(3)
    print(c)
    print(type(bin(3)))
