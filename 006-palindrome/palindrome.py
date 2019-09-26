# coding: utf-8
'''
leetcode: 125
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

经典回文，注意要越过非字母字符
'''
def palindrome(s):
    if not s:
        return True
    f, p = 0, len(s) -1
    a = 'qwertyuioplkjhgfdsazxcvbnm'
    s = s.lower()

    while f != p and p > f:
        if s[f] in a and s[p] in a:
            if s[f] == s[p]:
                f += 1
                p -= 1
            else:
                return False
        elif s[f] in a:
            p -= 1
        elif s[p] in a:
            f += 1
        else:
            f += 1
            p -= 1
    if s[f] in a and s[p] in a and s[f] != s[p]:
        return False
    return True


if __name__== "__main__":
    print(palindrome('OP'))
