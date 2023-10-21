""" AVL Tree implemented on top of the standard BST. """

__author__ = 'Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from bst import BinarySearchTree
from typing import TypeVar, Generic
from node import AVLTreeNode

K = TypeVar('K')
I = TypeVar('I')


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ Self-balancing binary search tree using rebalancing by sub-tree
        rotations of Adelson-Velsky and Landis (AVL).
    """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        BinarySearchTree.__init__(self)

    def get_height(self, current: AVLTreeNode) -> int:
        """
            Get the height of a node. Return current.height if current is 
            not None. Otherwise, return 0.
            :complexity: O(1)
        """

        if current is not None:
            return current.height
        return 0

    def get_balance(self, current: AVLTreeNode) -> int:
        """
            Compute the balance factor for the current sub-tree as the value
            (right.height - left.height). If current is None, return 0.
            :complexity: O(1)
        """

        if current is None:
            return 0
        return self.get_height(current.right) - self.get_height(current.left)

    def insert_aux(self, current: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert
            it. After insertion, performs sub-tree rotation whenever it becomes
            unbalanced.
            returns the new root of the subtree.
            Time Complexity of AVLTree insertion is O(log n)
        """
        if current is None:  # base case: at the leaf
            current = AVLTreeNode(key, item)
            self.length += 1
        elif key < current.key:
            current.left_nodes_total += 1
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right_nodes_total += 1
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            self.undo_insert_count(self.root, key)
            raise ValueError('Inserting duplicate item')

        # Update the height after inserting
        current.height = max(self.get_height(current.left),self.get_height(current.right)) + 1

        # Check if rebalncing needs to be done
        if self.get_balance(current) >= 2 or self.get_balance(current) <= -2:
                return self.rebalance(current)

        return current
    
    def undo_insert_count(self, current: AVLTreeNode, key: K)->None:
        """
        To undo the added left and right nodes total if the insertion did not happen (error duplicate key)
        Time Complexity is O(log n) where n is the number of nodes in the tree
        """
        if key < current.key:
            current.left_nodes_total -= 1
            current.left = self.undo_insert_count(current.left, key)
        elif key > current.key:
            current.right_nodes_total -= 1
            current.right = self.undo_insert_count(current.right, key)
        else:
            return


    def delete_aux(self, current: AVLTreeNode, key: K) -> AVLTreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete. After deletion,
            performs sub-tree rotation whenever it becomes unbalanced.
            returns the new root of the subtree.
            Time Complexity is O(log n), where n is the number of nodes in the tree
        """

        if current is None:  # key not found
            self.undo_delete_count(self.root, key)
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left_nodes_total -= 1
            current.left  = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right_nodes_total -= 1
            current.right = self.delete_aux(current.right, key)
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            # general case => find a successor

            # First save the successor
            save = self.get_successor(current)

            # Check if the successor's successor is none
            # if it is, we need to set the predecessor as the root
            # if this is not done, the tree will be unbalanced
            if self.get_successor(save) is None:
                succ = self.get_predecessor(current)
                current.left = self.delete_aux(current.left, succ.key)
                current.key  = succ.key
                current.item = succ.item
            else:
                succ = self.get_successor(current)
                current.key  = succ.key
                current.item = succ.item
                current.right = self.delete_aux(current.right, succ.key)

        # Update the height after deleting
        current.height = max(self.get_height(current.left),self.get_height(current.right)) + 1

        # Check if rebalancing needs to be done
        if self.get_balance(current) >= 2 or self.get_balance(current) <= -2:
                return self.rebalance(current)

        return current
    
    def undo_delete_count(self, current: AVLTreeNode, key: K)->None:
        """
        To undo the added left and right nodes total if the deletion did not happen (error key not found)
        Time Complexity is O(log n) where n is the number of nodes in the tree
        """
        if key < current.key:
            current.left_nodes_total += 1
            current.left = self.undo_delete_count(current.left, key)
        elif key > current.key:
            current.right_nodes_total += 1
            current.right = self.undo_delete_count(current.right, key)
        else:
            return

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform left rotation of the sub-tree.
            Right child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                 current                                       child
                /       \                                      /   \
            l-tree     child           -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree                 l-tree     center

            :complexity: O(1)
        """

        # Find child and center
        r_child = current.right
        center = r_child.left

        # Perform rotation
        r_child.left = current
        current.right = center
        
        # Update height
        current.height = max(self.get_height(current.left),self.get_height(current.right)) + 1
        current.left_nodes_total = self.get_size_left(current)
        current.right_nodes_total = self.get_size_right(current)

        r_child.height = max(self.get_height(r_child.left),self.get_height(r_child.right)) + 1
        r_child.left_count = self.get_size_left(r_child)
        r_child.right_count = self.get_size_right(r_child)

        return r_child

    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform right rotation of the sub-tree.
            Left child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                       current                                child
                      /       \                              /     \
                  child       r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree

            :complexity: O(1)
        """

        # Find child and center
        l_child = current.left
        center = l_child.right

        # Perform rotation
        l_child.right = current 
        current.left = center

        # Update height
        current.height = max(self.get_height(current.left),self.get_height(current.right)) + 1
        current.left_nodes_total = self.get_size_left(current)
        current.right_nodes_total = self.get_size_right(current)

        l_child.height = max(self.get_height(l_child.left),self.get_height(l_child.right)) + 1
        l_child.left_nodes_total = self.get_size_left(l_child)
        l_child.right_nodes_total = self.get_size_right(l_child)

        return l_child

    def get_size_left(self, current: AVLTreeNode):
        """
        Gets the size (total number of nodes) under a node
        Time Complexity is O(n) where n is the number of nodes in the tree
        """
        if self.is_leaf(current) or current.left == None:
            return 0
        else:
            return 1 + self.get_size_left(current.left) + self.get_size_right(current.left) 
    
    def get_size_right(self, current: AVLTreeNode):
        """
        Gets the size (total number of nodes) under a node
        Time Complexity is O(n) where n is the number of nodes in the tree
        """
        if self.is_leaf(current) or current.right == None:
            return 0
        else:
            return 1 + self.get_size_left(current.right) + self.get_size_right(current.right)  

    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate
            returns the new root of the subtree.
        """
        
        if self.get_balance(current) >= 2:
            child = current.right
            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)
            return self.left_rotate(current)

        if self.get_balance(current) <= -2:
            child = current.left
            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)
            return self.right_rotate(current)

        return current

    def kth_largest(self, k: int) -> AVLTreeNode:
        """
        Returns the kth largest element in the tree.
        k=1 would return the largest.
        Time Complexity is O(log(n)).
        The approach used for the kth_largest is log n.
        So, the total time complexity is O(log n)
        """
        return self.kth_largest_aux(k, self.root)

    def kth_largest_aux(self, k: int, current: AVLTreeNode):
        """
        If the k is equal to the amount of nodes in the right subtree + 1 it will return the current node
        Then, if the k is less than the total amount of nodes in the right, it will do recursion to the right subtree
        Else, it will do recursion to the left of the subtree, and change the k by a formula
        Because the left and right nodes total count is an instance variable, it is O(1)
        With the approach used, the time complexity is O(log n)
        """
        # The right subtree contains k - 1 elements higher than the root
        # If there right_nodes_total == k - 1
        # Return the value of the root
        if current.right_nodes_total == k - 1:
            return current
        # If the amount of right nodes is more than or equal to k, kth largest is in the right subtree
        # Recursively call kth largest to return kth largest
        if current.right_nodes_total >= k:
            if current.right is None:                #if right node is None, just return None
                return current
            return self.kth_largest_aux(k, current.right)
        # If amount of right nodes less than k, kth largest is in the left subtree
        # Recursively call kth largest to return kth largest
        else:
            if current.left is None:                 #if left node is None, just return None
                return current
            return self.kth_largest_aux(k - current.right_nodes_total - 1, current.left)
        

# b = AVLTree()
# # b[17] = "A"
# b[10] = "B"
# b[5] = "C"
# b[25] = "D"
# b[1] = "E"
# # b[21] = "F"
# # b[19] = "G"
# # b[23] = "H"

# b.draw()

# # print(b.kth_largest(1))
# b.delete_aux(b.root, 25)
# b.draw()

# b.delete_aux(b.root, 13)
# b.draw()

# b.delete_aux(b.root, 10)
# b.draw()



# print(b.get_successor(b.root))

# b.delete_aux(b.root, 20)
# b.draw()



# b.right_rotate((10, 'F'))
# b.draw()

# b.delete_aux(b.root, 25)
# b.draw()

# print(b.get_predecessor(b.root))

# b.delete_aux(b.root, 25)
# b.draw()

# b.delete_aux(b.root, 20)

# b.draw()

# b = AVLTree()
# b[15] = "A"
# b[10] = "B"
# b[20] = "C"
# b[17] = "D"
# b[5] = "E"
# b[3] = "F"
# b[4] = "G"
# b[22] = "H"

# b.draw()

# print(b.get_height(b.root.right))
# print(b.get_height(b.root.left))

# print(b.get_balance(b.root.right))
# print(b.get_balance(b.root.left))

# print(b.get_height(b.root.left))
# print(b.get_balance(b.root))
# b.rebalance(b.root)

# b.draw()

# b.rebalance(b.root)

# b.draw()



