# -*- encoding: utf-8 -*-
# 二叉树遍历


def pre_order(head):
    if head:
        stack = [head]
        while len(stack) != 0:
            head = stack.pop()
            print(head)
            if head.right:
                stack.append(head.right)
            if head.left:
                stack.append(head.left)


def in_order(head):
    if head:
        stack = []
        while len(stack) != 0 or head:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                print(head)
                stack.append(head.right)


def post_order(head):
    if head:
        last = head
        stack = [head]
        while len(stack) != 0:
            c = stack[-1]
            if c.left and c.left != last and c.right != last:
                stack.append(c.left)
            elif c.right and c.right != last:
                stack.append(c.right)
            else:
                print(stack.pop())
                last = c
