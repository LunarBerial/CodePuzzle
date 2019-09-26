#coding: utf-8
'''
leetcode: 203 https://leetcode.com/problems/remove-linked-list-elements/description/
解：链表问题。去掉链表中同给定值相同的值
'''

class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None


def ReverseList(head:ListNode):
    if not head:
        return head


    while head.next:
        pre = ListNode(None)
        curr = head

        tempNode = head.next
        pre = curr
        curr = tempNode

    return curr




if __name__=="__main__":
    head  = ListNode(1)
    cur = ListNode(2)
    head.next = cur
    for i in [1, 2, 4, 6, 7,3, 6]:
        cur.next = ListNode(i)
        cur = cur.next
    a = (RemoveTypicalValue(head, 6))
    while a.next:
        print(a.val)
        a = a.next
    print(a.val)
