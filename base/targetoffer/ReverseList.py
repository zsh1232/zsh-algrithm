# -*- encoding: utf-8 -*-
# 反转链表
#

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse(head):
    """
    1.递归方式反转链表
    :param head:
    :return:
    """
    if not head or not head.next:
        return head

    p = reverse(head.next)
    p.next = head
    head.next = None
    return head

def reverse2(head):
    """
    2.非递归反转链表
    :param head:
    :return:
    """
    pre, next = None, None
    cur = head
    while cur:
        next = cur.next
        cur.next = p
        p = cur
        cur = next


def printList(head):
    while head:
        print(head.val, )
        head = head.next


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    printList(head)
    reverse(head)