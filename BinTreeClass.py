# Sean A
# Binary Tree
# Create a Binary Tree datastructure

class BinaryTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    class BinaryNode:
        def __init__(self, data):
           self.__value = data

           self.__parent = None
           self.__left = None
           self.__right = None

        def __set_parent(self, node):
            """Changes the node's parent"""
            if node is None:
                self.__parent = node
            elif not isinstance(node, BinaryTree.BinaryNode):
                raise TypeError("The parent must be a node")
            elif node in (self.__right, self.__left):
                raise Exception("This node is already set to be a child")
            else:
                self.__parent = node

        def __set_left(self, node):
            """Changes the node's left child"""
            if node is None:
                self.__left = None
            elif not isinstance(node, BinaryTree.BinaryNode):
                raise TypeError("Left child must be a node")
            elif node is self.__right:
                raise Exception("This node is already set to be the right child")
            elif node is self.__parent:
                raise Exception("The parent cannot be a child of the node")
            else:
                self.__left = node

        def __set_right(self, node):
            """Changes the node's parent"""
            if node is None:
                self.__right = None
            elif not isinstance(node, BinaryTree.BinaryNode):
                raise TypeError("Right child must be a node")
            elif node is self.__right:
                raise Exception("This node is already set to be the left child")
            elif node is self.__parent:
                raise Exception("The parent cannot be a child of the node")
            else:
                self.__right = node

        def __str__(self):
            """Display to enable view for whole tree"""
            return f"|{self.__value}| \n({self.__value})L: {self.__left} \n({self.__value})R: {self.__right}"


    class Position:
        def __init__(self, tree, node):
            self.__member_of = tree
            self.__node = node


        def get_value(self):
            """Gets the value of the encapsulated node object"""
            return self.__node._BinaryNode__value

        def __eq__(self, other):
            """Returns true if two positions with the same value are given"""
            if isinstance(other, BinaryTree.Position):
                return self.get_value() == other.get_value()
            else:
                return False

        def __ne__(self, other):
            """Returns false if two given objects are not equal"""
            return not(self == other)

        def __str__(self):
            """Display position as value in node"""
            return str(self.get_value())

        def __repr__(self):
            """Display position when in collection"""
            return str(self)

    def __make_position(self, node):
        """Encapsulates a node object into a position object"""
        if isinstance(node, BinaryTree.BinaryNode):
            return BinaryTree.Position(self, node)
        else:
            return None

    def __validate(self, position):
        """Returns a boolean if an object is a valid position inside of the tree"""
        if not isinstance(position, BinaryTree.Position):
            raise TypeError("The given object is not a position")
        elif position._Position__member_of is not self:
            raise Exception("This position is not in the current tree!")
        elif position._Position__node._BinaryNode__parent == position._Position__node:
            raise Exception("The given position object does not exist")
        else:
            return position._Position__node

    def is_root(self, pos):
        """Returns a boolean if the given position is the tree's root"""
        node = self.__validate(pos)

        if node is self.__root:
            return True
        else:
            return False

    def is_leaf(self, pos):
        """Returns a boolean if the given position contains a leaf node"""
        node = self.__validate(pos)

        if node._BinaryNode__left is None and node._BinaryNode__right is None:
            return True
        else:
            return False

    def is_ancestor(self, ancestor, descendant):
        """Returns a boolean if the given position is an ancestor of the given descendent"""
        ancestor = self.__validate(ancestor)
        descendant = self.__validate(descendant)._BinaryNode__parent

        while descendant is not ancestor and descendant is not None:
            descendant = descendant._BinaryNode__parent

        if descendant is ancestor:
            return True
        else:
            return False

    def are_siblings(self, sibling1, sibling2):
        """Returns a boolean if the given positions have sibling nodes"""
        sibling1 = self.__validate(sibling1)
        sibling2 = self.__validate(sibling2)

        if (sibling1._BinaryNode__parent is sibling2._BinaryNode__parent) and sibling1 is not sibling2:
            return True
        else:
            return False

    def num_children(self, pos):
        """Returns the amount of children the position's node has"""
        node = self.__validate(pos)

        children = 0
        if node._BinaryNode__left is not None:
            children += 1
        if node._BinaryNode__right is not None:
            children += 1

        return children

    def get_root(self):
        """Returns the root node of the tree as a position"""
        return self.__make_position(self.__root)

    def get_left(self, pos):
        """Returns the left child of the given position"""
        node = self.__validate(pos)

        return self.__make_position(node._BinaryNode__left)

    def get_right(self, pos):
        """Returns the right child of the given position"""
        node = self.__validate(pos)

        return self.__make_position(node._BinaryNode__right)

    def get_parent(self, pos):
        """Returns the parent of the given position"""
        node = self.__validate(pos)

        return self.__make_position(node._BinaryNode__parent)

    def get_children(self, pos):
        """Returns a list of all children of the given position"""
        node = self.__validate(pos)

        children = []

        if node._BinaryNode__left is not None:
            children.append(self.__make_position(node._BinaryNode__left))

        if node._BinaryNode__right is not None:
            children.append(self.__make_position(node._BinaryNode__right))

        if len(children) == 0:
            return None

        return children

    def get_sibling(self, pos):
        """Returns the sibling of the given position"""
        node = self.__validate(pos)
        parent = node._BinaryNode__parent
        sibling = None

        if not parent:
            return None
        elif parent._BinaryNode__left is node:
            sibling = parent._BinaryNode__right

        elif parent._BinaryNode__right is node:
            sibling = parent._BinaryNode__left

        return self.__make_position(sibling)

    def get_ancestors(self, pos):
        """Returns the ancestors of the given position"""
        node = self.__validate(pos)._BinaryNode__parent
        ancestors = []

        if node is None:
            return None
        while node is not None:
            ancestors.append(self.__make_position(node))
            node = node._BinaryNode__parent

        return ancestors

    def get_depth(self, pos):
        """Returns the depth of the given position"""
        if self.get_ancestors(pos) is None:
            return 0
        else:
            return len(self.get_ancestors(pos))

    def add_root(self, val):
        """Adds a root to the tree, if the tree has no root"""
        if self.__root:
            raise Exception("This tree already has a a root")
        else:
            self.__root = BinaryTree.BinaryNode(val)
            self.__size += 1
            return self.__make_position(self.__root)

    def add_left(self, parent, value):
        """Adds a left child to the given position"""
        parent = self.__validate(parent)
        if parent._BinaryNode__left:
            raise Exception("This object already has a left child")
        else:
            leftNode = BinaryTree.BinaryNode(value)
            leftNode._BinaryNode__set_parent(parent)
            parent._BinaryNode__set_left(leftNode)
            self.__size += 1

            return self.__make_position(leftNode)

    def add_right(self, parent, value):
        """Adds a right child to the given position"""
        parent = self.__validate(parent)
        if parent._BinaryNode__right:
            raise Exception("This object already has a right child")
        else:
            rightNode = BinaryTree.BinaryNode(value)
            rightNode._BinaryNode__set_parent(parent)
            parent._BinaryNode__set_right(rightNode)
            self.__size += 1

            return self.__make_position(rightNode)

    def replace(self, pos, value):
        """Replaces the value in the position's node"""
        node = self.__validate(pos)

        oldVal = pos.get_value()
        node._BinaryNode__value = value

        return oldVal

    def delete(self, pos):
        """Removes the position's node from the tree"""
        node = self.__validate(pos)
        if node._BinaryNode__left and node._BinaryNode__right:
            raise Exception("The node you are trying to delete has two children")
        else:
            child = node._BinaryNode__left if node._BinaryNode__left is not None else node._BinaryNode__right
            parent = node._BinaryNode__parent

            if not parent:
                self.__root = None
            elif parent._BinaryNode__left is node:
                if child:
                    parent._BinaryNode__set_left(child)
                    child._BinaryNode__set_parent(parent)
                else:
                    parent._BinaryNode__set_left(None)
            elif parent._BinaryNode__right is node:
                if child:
                    parent._BinaryNode__set_right(child)
                    child._BinaryNode__set_parent(parent)
                else:
                    parent._BinaryNode__set_right(None)

            node._BinaryNode__set_parent(node)
            self.__size -= 1
            return pos.get_value()


    def __len__(self):
        """Returns the size of the tree"""
        return self.__size

    def __str__(self):
        """Convert root to string"""
        return str(self.__root)
