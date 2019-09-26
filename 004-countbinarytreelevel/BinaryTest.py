# coding : utf-8

class Node():
    def __init__(self, value=None):
        self.value = value
        self.leftchild = None
        self.rightchild = None

class Tree():
    def __init__(self):
        self.root = Node()
        self.MyQueue = []

    def add(self, elem):
        node = Node(elem)
        if self.root.value == None:
            self.root = node
            self.MyQueue.append(self.root)
        else:
            treeNode = self.MyQueue[0]
            if treeNode.leftchild == None:
                treeNode.leftchild = node
                self.MyQueue.append(treeNode.leftchild)
            else:
                treeNode.rightchild = node
                self.MyQueue.append(treeNode.rightchild)
                self.MyQueue.pop(0)

def MaxDepth(root):
    if root is None:
        return 0

    else:
        left_height = MaxDepth(root.leftchild)
        right_height = MaxDepth(root.rightchild)
        return max(left_height, right_height) + 1


if __name__=="__main__":
    elements = [3, 9, 20, None, None, 15, 7]
    tree = Tree()
    for elem in elements:
        tree.add(elem)


