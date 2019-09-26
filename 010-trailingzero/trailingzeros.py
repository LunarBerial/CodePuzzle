#coding: utf-8
'''
leetcode: 172
https://leetcode.com/problems/factorial-trailing-zeroes/description/
限制时间复杂度为O(logn)
思路：求给定数n的阶乘中末尾会出现多少个0.经观察得到2x5=10，故因式分解后阶乘中有多少2和5就会有多少个0.又因2的个数肯定比5多，所以只计算5的个数。
注意：python3和2的除法符号的不同含义
'''

'''
方法1：令n直接除以5取整，为算出其中包括多少5的倍数。而后循环除以5取整，是为了得到5的幂次中含5的个数。
'''
def trailingzeros(n: int):
    count = 0
    while n >=5:
        count += int(n/5)
        n = int(n/5)
    return count


def trailingzeros_2(n: int):
    if n < 5:
        return 0
    else:
        return int(n/5) + trailingzeros_2(int(n/5))

if __name__=="__main__":
    print(trailingzeros_2(555))
    print(trailingzeros(555))