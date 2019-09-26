# coding: utf-8

'''
leetcode : 155
https://leetcode-cn.com/problems/min-stack/solution/shi-yong-fu-zhu-zhan-tong-bu-he-bu-tong-bu-python-/
构建一个栈，实现pop, push, top和getmini的操作
注：需要检查stack非空，否则会越界。
'''

class Ministack:
    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, x):
        self.stack.append(x)
        if (not self.mini) or self.mini[-1] >= x:
            self.mini.append(x)
        else:
            self.mini.append(self.mini[-1])

    def pop(self):
        if self.stack:
            self.mini.pop(-1)
        return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getmini(self):
        if self.mini:
            return self.mini[-1]
        else:
            return None


if __name__ == "__main__":
    teststack = Ministack()
    print(teststack.top())
