#coding: utf-8


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


def ispoweroffour2(n:int):

    binnum = bin(n)[2:]
    return binnum.strip('0') == '1' and len(binnum)%2 == 1