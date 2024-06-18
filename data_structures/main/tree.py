class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node :
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # percurso em ordem simetrica
    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.inorder(node.left)
        print(node, end='')
        if node.right:
            self.inorder(node.right)
            print(')', end='')

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

def postorder_example_tree():
        tree = BinaryTree()
        n1 = Node('I')
        n2 = Node('N')
        n3 = Node('S')
        n4 = Node('C')
        n5 = Node('R')
        n6 = Node('E')
        n7 = Node('V')
        n8 = Node('A')
        n9 = Node('-')
        n10 = Node('5')
        n0 = Node('3')

        n0.left = n6
        n0.right = n10
        n6.left = n1
        n6.right = n5
        n5.left = n2
        n5.right = n4
        n4.right = n3
        n10.left = n8
        n10.right = n9
        n8.right = n7

        tree.root = n0
        return tree

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value <x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        elif node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)


if __name__ == "__main__":
    tree = postorder_example_tree()
    print("Percurso em pós ordem: ")
    tree.postorder_traversal()