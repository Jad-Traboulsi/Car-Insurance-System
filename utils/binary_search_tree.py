class BSTNode:
    def __init__(self, key, value):
        self.key = key    # For example, client name (lowercase)
        self.value = value  # The actual Client object
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, value)
            else:
                self._insert(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, value)
            else:
                self._insert(node.right, key, value)
        else:
            # If key already exists, overwrite or handle differently
            node.value = value

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._find(node.left, key)
        elif key > node.key:
            return self._find(node.right, key)
        else:
            return node.value

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Found the node to delete
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node has two children
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def in_order_traversal(self, visit_fn=None):
        """
        If visit_fn is provided, call visit_fn(node.value).
        Otherwise, just print the node value.
        """
        self._in_order(self.root, visit_fn)

    def _in_order(self, node, visit_fn):
        if node is not None:
            self._in_order(node.left, visit_fn)
            if visit_fn:
                visit_fn(node.value)
            else:
                print(node.value)
            self._in_order(node.right, visit_fn)
