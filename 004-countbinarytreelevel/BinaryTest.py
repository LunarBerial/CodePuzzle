# coding : utf-8

class Node():
    def __init__(self, value=None, leftchild=None, rightchild= None):
        self.value = value
        self.leftchild = leftchild
        self.rightchild = rightchild


class Tree():
    def __init__(self):
        self.root = Node()
        self.elements = []
        self.layer_num = 0
    def add(self, ele):

        if not self.root:
            self.root = ele[0]

        while ele:

