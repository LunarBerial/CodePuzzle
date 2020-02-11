#coding: utf-8
# leetcode 342: https://leetcode.com/problems/power-of-four/description/ 判断一个数是否为4的幂

#方法1：递归除4：
def ispoweroffour_raw(n:int):
    while(n && n%4 == 0):
        n = n/4
    return n == 1

#方法 2： 如果不让用递归的方式。换一种思路：那么4的幂一定是2的幂。 并且 该数 - 1一定是3的幂。
def ispoweroffour(n:int):

    if n == 1:
        return True
    elif n < 4:
        return False
    else:
        if n%2==0 and (n-1)%3 == 0:
            return True
        else:
            return False

# 方法3： 转化为2进制。4的幂数一定满足有奇数个1.
def ispoweroffour2(n:int):

    binnum = bin(n)[2:]
    return binnum.strip('0') == '1' and len(binnum)%2 == 1
