# codig: utf-8

'''
leetcode:263
对给定的数做因式分解。若该数的因子中存在不等于2， 3， 5的数，则返回False, 否则返回True。
'''
def uglynumber(k:int):
    # 加判断，非正数不参与后续运算
    if k <=0:
        return False
    for i in (2, 3, 5):
        while k%i == 0:
            k = k/ i

    return k == 1


if __name__=="__main__":
    print(uglynumber(11))