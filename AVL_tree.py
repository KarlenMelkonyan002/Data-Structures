from node import Node


class AVLTree(Node):

    def get_height(self, root):
        if not root:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    @staticmethod
    def right_rotate(node):
        left_ = node.left
        right_ = left_.right
        left_.right = node
        node.left = right_
        return left_

    @staticmethod
    def left_rotate(node):
        right_ = node.right
        left_ = right_.left
        right_.left = node
        node.right = left_
        return right_

    def insert(self, val, root):
        if not root:
            return Node(val)
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        else:
            root.right = self.insert(val, root.right)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and val < root.left.value:
            return self.right_rotate(root)
        if balance < -1 and val > root.right.value:
            return self.left_rotate(root)
        if balance > 1 and val > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and val < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def clear(self, root):
        if root is not None:
            self.clear(root.left)
            self.clear(root.right)
            del root

    def erase(self, root, key):
        if not root:
            return root
        elif key < root.value:
            root.left = self.erase(root.left, key)
        elif key > root.value:
            root.right = self.erase(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_node(root.right)
            root.value = temp.value
            root.right = self.erase(root.right, temp.value)
        if root is None:
            return root
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance = self.get_balance(root)
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_node(self, root):
        if root is None or root.left is None:
            return root
        return self.min_node(root.left)

    def get_number_of_nodes(self, root):
        if not root:
            return 0
        return 1 + self.get_number_of_nodes(root.left) + self.get_number_of_nodes(root.right)

    def preorder(self, root, arr):
        if not root:
            return
        arr.append(root.value)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)
        return arr

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value)

    def current_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.value)
        elif level > 1:
            self.current_level(root.left, level - 1)
            self.current_level(root.right, level - 1)

    def levelorder(self, root):
        height = self.get_height(root)
        for i in range(height + 1):
            self.current_level(root, i)

    @staticmethod
    def get_root_data(root):
        return root.value

    def merge(self, other):
        pass

    def contains(self, node, key):
        if not node:
            return False
        if node.value == key:
            return True
        ans1 = self.contains(node.left, key)
        if ans1:
            return True
        ans2 = self.contains(node.right, key)
        return ans2

    def find(self, node, key):
        if not node:
            return False
        if node.value == key:
            return node.value
        ans1 = self.find(node.left, key)
        if ans1:
            return node.left
        ans2 = self.find(node.right, key)
        return ans2

    def __eq__(self, other):
        if self is None and other is None:
            return True
        if self is not None and other is not None:
            return self.preorder(root_, []) == other.preorder(root__, [])

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        tree_1 = self.preorder(root_, [])
        tree_2 = other.preorder(root__, [])
        return [i + j for i, j in zip(tree_1, tree_2)]

    def __iadd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f"{self.preorder(root__, [])}"


# Tree.preorder(root_)
# Tree.inorder(root_)
# print(Tree.get_height(root_))
# print(Tree.clear(root_))
Tree1 = AVLTree()

root__ = None
root__ = Tree1.insert(10, root__)
root__ = Tree1.insert(20, root__)
root__ = Tree1.insert(30, root__)
root__ = Tree1.insert(40, root__)
root__ = Tree1.insert(50, root__)
root__ = Tree1.insert(25, root__)
Tree = AVLTree()
root_ = None
root_ = Tree.insert(10, root_)
root_ = Tree.insert(20, root_)
root_ = Tree.insert(30, root_)
root_ = Tree.insert(40, root_)
root_ = Tree.insert(50, root_)
root_ = Tree.insert(100, root_)
# Tree.preorder(root_)
# Tree.inorder(root_)
# print(Tree.get_height(root_))
# print(Tree.clear(root_))
print(Tree.preorder(root_, []))
print("-----------------------------------------------------------------------------")
print(Tree1.preorder(root__, []))
print("-----------------------------------------------------------------------------")
print(Tree1 == Tree)
print(Tree1)
