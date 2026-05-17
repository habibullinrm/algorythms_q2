from math import inf
from multiprocessing import heap

import numpy as np
import sys


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def search(node, target):
    if node is None:
        return None
    if node.value == target:
        return node
    if target < node.value :
        return search(node.left, target)
    else:
        return search(node.right, target)

def insert(node, val):
    if node is None:
        return Node(val)
    if val < node.value :
        return insert(node.left, val)
    elif val > node.value :
        return insert(node.right, val)
    return node


def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def find_max(node):
    while node.right is not None:
        node = node.right
    return node

def find_ios(node):
    if node.right is None:
        return None
    return find_min(node.right)

def find_iop(node):
    if node.left is None:
        return None
    return find_max(node.left)

def delete(node, value):
    if node is None:
        return None
    
    if value < node.value :
        node.left = delete(node.left, value)
    elif value > node.value :
        node.right = delete(node.right, value)
    else:
        if node.left is None and node.right is None:
            return None
        if node.left is None:
            return node.right
        
        successor = find_min(node.right)
        node.value = successor.value 
        node.right = delete(node.right, successor.value )
    return node

def pre_order(node):
    if node is None:
        return
    print(node.value ) # 1. выводим значение текущей вершины
    pre_order(node.left) # 2. идём в левое поддерево
    pre_order(node.right) # 3. идём в правое поддерево

def in_order(node):
    if node is None:
        return
    in_order(node.left) # 1. сначала весь левый поддерев
    print(node.value ) # 2. потом текущая вершина
    in_order(node.right) # 3. потом весь правый поддерев

def post_order(node):
    if node is None:
        return
    post_order(node.left) # 1. сначала весь левый поддерев
    post_order(node.right) # 2. потом весь правый поддерев
    print(node.value ) # 3. и только в конце — текущая вершина


# ========================================================================================

class Node:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value


def insert(root, value):
    if root is None:
        return Node(value)
    cur = root
    while True:
        if value < cur.value:
            if cur.left is None:
                cur.left = Node(value, parent=cur)
                return root
            cur = cur.left
        elif value > cur.value:
            if cur.right is None:
                cur.right = Node(value, parent=cur)
                return root
            cur = cur.right
        else:
            return root

def in_order(root):
    result = []
    stack = []
    cur = root
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.value)
        cur = cur.right
    return result

def leaves_in_order(root):
    result = []
    stack = []
    cur = root
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        if cur.left is None and cur.right is None:
            result.append(cur.value)
        cur = cur.right
    return result

def one_child_in_order(root):
    result = []
    stack = []
    cur = root
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        if int(cur.left is None) + int(cur.right is None) == 1:
            result.append(cur.value)
        cur = cur.right
    return result

def height(root):
    if root is None:
        return 0
    queue = deque([root])
    levels = 0
    while queue:
        levels += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return levels

def is_balanced(root):
    if root is None:
        return True

    heights = {}                  
    stack = [(root, False)]       

    while stack:
        node, processed = stack.pop()
        if processed:
            lh = heights[id(node.left)]  if node.left  is not None else 0
            rh = heights[id(node.right)] if node.right is not None else 0
            if abs(lh - rh) > 1:
                return False
            heights[id(node)] = 1 + max(lh, rh)
        else:
            stack.append((node, True))
            if node.right is not None:
                stack.append((node.right, False))
            if node.left is not None:
                stack.append((node.left, False))

    return True

        
def second_largest(root):
    if root is None or (root.left is None and root.right is None):
        return None

    parent = None
    cur = root
    while cur.right is not None:
        parent = cur
        cur = cur.right
   
    if cur.left is not None:
        node = cur.left
        while node.right is not None:
            node = node.right
        return node.value

    return parent.value

def in_order_2(root):

    if root is None:
        return

    cur = root
    while cur.left is not None:
        cur = cur.left

    out = sys.stdout.write
    sep = ''                       
    while cur is not None:
        out(sep + str(cur.value))
        sep = ' '                  

        if cur.right is not None:
            cur = cur.right
            while cur.left is not None:
                cur = cur.left
        else:
            while cur.parent is not None and cur.parent.right is cur:
                cur = cur.parent
            cur = cur.parent 
    out('\n')


def build_from_postorder(post):
    if not post:
        return None

    root = Node(post[-1])
    stack = [root]

    for i in range(len(post) - 2, -1, -1):
        val = post[i]
        cur = Node(val)

        if val > stack[-1].value:
            stack[-1].right = cur
        else:
            parent = None
            while stack and stack[-1].value > val:
                parent = stack.pop()
            parent.left = cur

        stack.append(cur)

    return root



def ex_1():
    numbers = [int(x) for x in input().strip().split()]

    node = None
    for x in numbers:
        node = insert(node, x)
    
    print(' '.join(map(str, in_order(node))))

def ex_2():
    numbers = [int(x) for x in input().strip().split()]

    node = None
    for x in numbers:
        node = insert(node, x)
    
    print(' '.join(map(str, leaves_in_order(node))))

def ex_3():
    numbers = [int(x) for x in input().strip().split()]

    node = None
    for x in numbers:
        node = insert(node, x)
    
    print(' '.join(map(str, one_child_in_order(node))))


def ex_4():
    numbers = [int(x) for x in input().strip().split()]

    node = None
    for x in numbers:
        node = insert(node, x)
    
    print(1 + max(height(node.left), height(node.right)))

def ex_5():
    numbers = [int(x) for x in input().strip().split()]
    node = None
    for x in numbers:
        node = insert(node, x)
    print('YES' if abs(height(node.left) - height(node.right)) <= 1 else 'NO')

def ex_6():
    numbers = [int(x) for x in input().strip().split()]
    node = None
    for x in numbers:
        node = insert(node, x)
    result = second_largest(node)
    
    print(result)


def ex_7():
    numbers = [int(x) for x in input().strip().split()]
    node = None
    for x in numbers:
        node = insert(node, x)
    in_order_2(node)


def ex_8():
    numbers = [int(x) for x in input().strip().split()]
    result = build_from_postorder(numbers)
    if result is None:
        return None
    
    print(' '.join(map(str, leaves_in_order(result))))

def ex_9():
    pass

def ex_10():
    pass

import math
from collections import deque
import sys

if __name__ == "__main__":
    ex_8()