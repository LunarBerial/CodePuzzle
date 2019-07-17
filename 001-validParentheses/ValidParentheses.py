# coding: utf-8
'''
leetcode - 0020
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

'''
def validParentheses(s):
    left_p = ('(', '{', '[')
    right_p = (')', '}', ']')

    v = [] # 用list来模拟栈的操作
    flag = True

    for s0 in s:
        if s0 in left_p:
            v.append(s0)
        elif s0 in right_p and v: # 若右向符号先于左向符号出现， False
            s1 = v.pop(-1)
            if not left_p.index(s1) == right_p.index(s0): # 若左右向不对等， False
                flag = False
                return flag
        else:
            flag = False
            return flag
    if v: # 若无右向匹配项， False
        flag = False
        return flag
    return flag


if __name__== "__main__":
    sa = ['()','()[]{}','(]','([)]','{[]}']
    for s in sa:
        print(validParentheses(s))

