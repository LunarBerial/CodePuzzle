#coding: utf-8

'''
leetcode 283
题解：将序列中所有的0移到序列末尾。不得使用额外内存
'''
def removezeros(n:list):
    co = n.count(0)
    while co > 0:
        idx = n.index(0)
        n.pop(idx)
        n.append(0)
        co -= 1
    return n


def removezeros2(n:list):
    j = 0
    for i in range(len(n)):
        if n[i] != 0:
            n[i], n[j] = n[j], n[i]
            j += 1

    return n

if __name__=="__main__":
    a = removezeros2([0,1,2,3,0,4,5])
    print(a)