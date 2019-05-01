class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        if self.parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 1


class Tree:
    def __init__(self, data_root):
        self.root = Node(data=data_root)

    def add_node(self, data, node):
        if data <= node.data:
            if node.left:
                self.add_node(data, node=node.left)
            else:
                node.left = Node(parent=node, data=data, left=None, right=None)
        else:
            if node.right:
                self.add_node(data, node=node.right)
            else:
                node.right = Node(parent=node, data=data, left=None, right=None)

    def bfs(self):
        queue = []
        p = self.root

        queue.append(p)

        while queue:
            temp = queue.pop(0)
            print('\t'*temp.depth, sep='')
            print(temp.data)

            if temp.left is not None:
                queue.append(temp.left)

            if temp.right is not None:
                queue.append(temp.right)

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


t = Tree(9)
# t.bfs()
t.add_node(7, t.root)
t.add_node(20, t.root)
t.add_node(2, t.root)
t.add_node(8, t.root)
t.add_node(15, t.root)
t.add_node(4, t.root)
t.add_node(12, t.root)
t.add_node(17, t.root)
t.add_node(3, t.root)
t.add_node(5, t.root)

t.print_in_order(t.root)


