#coding: utf-8
'''
leetcode: 203 https://leetcode.com/problems/remove-linked-list-elements/description/
解：链表问题。去掉链表中同给定值相同的值
'''

class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None


def RemoveTypicalValue(head:ListNode, val:int):
    if not head:
        return head


    pre = ListNode(0)
    pre.next = head
    while head.val == val and head.next:
        head = head.next

    while head.next:
        if head.next.val == val: #若当前值为目标值，删除链表节点
            head.next = head.next.next

        else:
            head = head.next # 若当前值不为目标值，指针向前移动一位

    return pre.next #返回链表的head


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
