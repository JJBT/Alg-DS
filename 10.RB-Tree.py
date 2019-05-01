"""Красно-черное дерево - бинарное дерево поиска, сбалансированное(h = O(log n) ~~ h <= 2log(n + 1))
 1. Каждый узел либо красный, либо черный
 2. Корень и листья (NIL) - черные
 3. У красного узла все дочерные узлы черные
 4. Для каждого узла все простые пути от него до листьев, содержат одно и то же кол-во черный узлов"""


class Node:
    def __init__(self, data=None, parent=None, left=None, right=None, color = None):
        self.data = data
        self.left = left
        self.right = right
        self.color = color  # 0 - black, 1 - red
        self.parent = parent
        if self.parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 1


class Tree:
    def __init__(self, data_root):
        self.root = Node(data=data_root)
        self.nil = Node()

    def left_rotate(self, x):
        """Предполагается x.right != T.nil"""
        y = x.right
        x.right = y.left

        if y.left:
            y.left.parent = x
        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def add_node(self, data, node):
        if data <= node.data:
            if node.left:
                self.add_node(data, node=node.left)
            else:
                node.left = Node(parent=node, data=data, color=1)
                # fix-up
        else:
            if node.right:
                self.add_node(data, node=node.right)
            else:
                node.right = Node(parent=node, data=data, color=1)
                # fix-up

    def r_bfs(self):
        queue = []
        p = self.root

        queue.append(p)

        while queue:
            temp = queue.pop(0)
            print('\t'*temp.depth, end='')
            print(temp.data)

            if temp.right:
                queue.append(temp.right)

            if temp.left:
                queue.append(temp.left)

    def depth_traversal(self, node):
        if node.right:
            self.depth_traversal(node.right)

        print('\t'*node.depth, end='')
        print(node.data)

        if node.left:
            self.depth_traversal(node.left)

    def search(self, data, temp_node=None):
        if not temp_node:
            temp_node = self.root

        if data == temp_node.data:
            return True

        if data < temp_node.data and temp_node.left:
            return self.search(data, temp_node.left)

        elif data > temp_node.data and temp_node.right:
            return self.search(data, temp_node.right)

        return False

    def print_in_order(self, node):
        """sorting  O(n)"""
        if node.left:
            self.print_in_order(node.left)
        print(node.data)
        if node.right:
            self.print_in_order(node.right)
