#coding: utf-8

'''
leetcode: 169
https://leetcode.com/problems/majority-element/description/
思路：若数组中一定存在某个数字出现超过一半以上，求该数。解：摩尔投票法
'''

def majorityelement(numbers:list):
    count = 0 # 待配对的数个数
    target = numbers[0] # 众数
    for i in numbers[1:]:
        if i == target:
            count += 1

        else:
            if count == 0:
                target = i
            else:
                count -= 1

    return target


if __name__== "__main__":
    a = majorityelement([3,2,3])
    print(a)