#coding: utf-8

def reversebit(n:int):
    n = list(bin(n)[2:])
    print(n)
    l_n = len(n)
    for i in range(int(l_n//2)):
        temp = n[i]
        n[i] = n[l_n - i - 1]
        n[l_n - i - 1] = temp
    print(n)
    n = int(''.join(n), 2)
    print(n)
    return n


if __name__=="__main__":
    reversebit(100)
