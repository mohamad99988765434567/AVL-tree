#username - Mahajna3
#id1      - 324887488
#name1    - Mohamad Mahajna
#id2      - 213127905
#name2    - Amana Essa


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
        """Constructor, you are allowed to add more fields.

        @type key: int or None
        @type value: any
        @param value: data of your node
        """
        def __init__(self, key, value):
                self.key = key
                self.value = value
                self.left = None
                self.right = None
                self.parent = None
                self.height = -1

        """returns the left child
        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child (if self is virtual)
        """
        def get_left(self):
                return self.left if self.is_real_node() else None



        """returns the right child

        @rtype: AVLNode
        @returns: the right child of self, None if there is no right child (if self is virtual)
        """

        def get_right(self):
                return self.right if self.is_real_node() else None


        """returns the parent 

        @rtype: AVLNode
        @returns: the parent of self, None if there is no parent
        """
        def get_parent(self):
                return self.parent


        """returns the key

        @rtype: int or None
        @returns: the key of self, None if the node is virtual
        """
        def get_key(self):
                return self.key if self.is_real_node() else None


        """returns the value

        @rtype: any
        @returns: the value of self, None if the node is virtual
        """
        def get_value(self):
                return self.value if self.is_real_node() else None


        """returns the height

        @rtype: int
        @returns: the height of self, -1 if the node is virtual
        """
        def get_height(self):
                return self.height if self.is_real_node() else -1


        """sets left child

        @type node: AVLNode
        @param node: a node
        """
        def set_left(self, node):
                self.left = node
                node.parent = self


        """sets right child

        @type node: AVLNode
        @param node: a node
        """
        def set_right(self, node):
                self.right = node
                node.parent = self



        """sets parent

        @type node: AVLNode
        @param node: a node
        """
        def set_parent(self, node):
                self.parent = node

        """sets key

        @type key: int or None
        @param key: key
        """
        def set_key(self, key):
                self.key = key


        """sets value

        @type value: any
        @param value: data
        """
        def set_value(self, value):
                self.value = value

        """sets the height of the node

        @type h: int
        @param h: the height
        """
        def set_height(self, h):
                self.height = h


        """returns whether self is not a virtual node 

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """
        def is_real_node(self):
                return self.key is not None
        """ calculates new height and sets it
        """
        def height_calculator(self):
                self.set_height( max(self.left.height ,self.right.height) +1)


        """ Calculate BlanceFactor and returns it 
        @rtype: int 
        @returns : BalanceFactor 
        """

"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

        """
        Constructor, you are allowed to add more fields.

        """
        def __init__(self):
                self.root = None
                self.size_count = 0
                # add your fields here



        """searches for a value in the dictionary corresponding to the key

        @type key: int
        @param key: a key to be searched
        @rtype: any
        @returns: the value corresponding to key.
        """
        def search(self,key):
                if self.root is None or self.root.key == None : # empty tree
                        return None
                current = self.root
                while current.get_key() is not None :
                        if current.get_key() == key:
                                return current
                        elif current.get_key() > key :
                                current = current.get_left()
                        else :
                                current=current.get_right()
                return None




        """inserts val at position i in the dictionary

        @type key: int
        @pre: key currently does not appear in the dictionary
        @param key: key of item that is to be inserted to self
        @type val: any
        @param val: the value of the item
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """

        def insert(self, key, val):
                node = AVLNode(key, val)
                node.set_height(0)
                vert1 = AVLNode(None, None)
                vert2 = AVLNode(None, None)
                if self.root is None or not self.root.is_real_node():
                        self.root = node
                        node.set_parent(None)
                        self.root.set_left(vert1)
                        self.root.set_right(vert2)
                        vert1.set_parent(self.root)
                        vert2.set_parent(self.root)
                        self.size_count+=1
                        return 0
                if self.regular_insert(node) is False:
                        return 0
                p = node.get_parent()
                son = node
                self.size_count += 1
                node.set_left(vert1)
                node.set_right(vert2)
                vert1.set_parent(node)
                vert2.set_parent(node)

                return self.Balance(p, son)

        def node_position(self, node, key):  # look for key "key" in the subtree of node
                # return the last node encountered
                curr= node
                while node.get_key() is not None:

                        curr = node
                        if key== node.key:
                                return False

                        if key < node.key:
                                node = node.left
                        else:
                                node = node.right
                return curr

        def regular_insert(self, node):
                new_p = self.node_position(self.root, node.key)# new parent
                if new_p is False:
                        return False
                node.set_parent(new_p)

                if node.key < new_p.key:
                        new_p.set_left(node)
                else:
                        new_p.set_right(node)
                return

        def BF(self, node):  # returns the balance factor of a node
                h1 = node.get_left().get_height() if node.get_left() else -1
                h2 = node.get_right().get_height() if node.get_right() else -1
                return h1 - h2

        def height_has_changed(self, node, son):  # checks if node`s height has changed after insertion
                return node.get_height() < son.get_height() + 1

        def rotate(self, node, son):  # performs rotation
                n_bf = self.BF(node)
                s_bf = self.BF(son)
                if n_bf > 0 and s_bf > 0  :
                        self.do_right_rotation(node, son)
                        node.height_calculator()
                        son.height_calculator()
                        return 1
                if n_bf < 0 and s_bf < 0  :
                        self.do_left_rotation(node, son)
                        node.height_calculator()
                        son.height_calculator()
                        return 1
                if n_bf > 0 and s_bf < 0:
                        grandson = son.get_right()
                        self.do_left_rotation(son, grandson)
                        self.do_right_rotation(node, grandson)
                        node.height_calculator()
                        son.height_calculator()
                        grandson.height_calculator()
                        return 2
                if n_bf < 0 and s_bf > 0:
                        grandson = son.get_left()
                        self.do_right_rotation(son, grandson)
                        self.do_left_rotation(node, grandson)
                        node.height_calculator()
                        son.height_calculator()
                        grandson.height_calculator()
                        return 2
                return 0
        def Balance(self, p, son):
                balance = 0  # to compute the number of balancing operations
                while p is not None:
                        bf = self.BF(p)
                        h_changed = self.height_has_changed(p, son)
                        if (abs(bf) < 2) and (h_changed is False):
                                return balance
                        if (abs(bf) < 2) and h_changed:
                                p.set_height(p.get_height() + 1)
                                balance += 1
                                son = p
                                p = p.get_parent()
                        else:
                                p.set_height(p.get_height() + 1)
                                balance += 1
                                balance += self.rotate(p, son)
                                return balance
                return balance

        def do_left_rotation(self, node, son): # do left_rotation
                if self.root == node:
                        self.root = son
                        son.set_parent(None)

                node_p = node.get_parent()
                grandson = son.get_left()
                node.set_right(grandson)
                grandson.set_parent(node)

                son.set_left(node)
                son.set_parent(node_p)

                if node_p is not None:
                        if node_p.get_left() == node:
                                node_p.set_left(son)
                        else:
                                node_p.set_right(son)

                node.set_parent(son)

                return

        def do_right_rotation(self, node, son): # do right_rotation
                if self.root == node:
                        self.root = son
                        son.set_parent(None)

                node_p = node.get_parent()
                grandson = son.get_right()
                node.set_left(grandson)
                grandson.set_parent(node)

                son.set_right(node)
                son.set_parent(node_p)

                if node_p is not None:
                        if node_p.get_left() == node:
                                node_p.set_left(son)
                        else:
                                node_p.set_right(son)

                node.set_parent(son)

                return
        def height_has_changed_delete (self,p) : # check if height changed
                orig_height = p.get_height()
                p.height_calculator()
                if orig_height != p.get_height() :
                        return True
                return False
        def Delete_Balance(self, p): # delete_balance
                balance = 0  # to compute the number of balancing operations
                while p is not None:
                        h_changed = self.height_has_changed_delete(p)
                        bf = self.BF(p)
                        if (abs(bf) < 2) and not h_changed :
                                return balance
                        if (abs(bf) < 2) and h_changed:
                                balance += 1
                                p = p.get_parent()
                        else:
                                parent = p.get_parent()
                                if bf == -2 :
                                        balance += self.delete_rotate(p,p.get_right())
                                else :
                                        balance += self.delete_rotate(p,p.get_left())
                                p = parent
                return balance
        """ Rebalnce
        @pre : node in self 
        @rtype:int 
        @returns: Number of rebalancing operations including fixing height and rotations
        """
        def delete_rotate(self, node, son):  # performs rotation
                n_bf = self.BF(node)
                s_bf = self.BF(son)
                if n_bf > 0 and s_bf > 0 or (n_bf > 0 and s_bf == 0) :
                        self.do_right_rotation(node, son)
                        node.height_calculator()
                        son.height_calculator()
                        return 1
                if n_bf < 0 and s_bf < 0 or (n_bf < 0 and s_bf == 0) :
                        self.do_left_rotation(node, son)
                        node.height_calculator()
                        son.height_calculator()
                        return 1
                if n_bf > 0 and s_bf < 0:
                        grandson = son.get_right()
                        self.do_left_rotation(son, grandson)
                        grandson.height_calculator()
                        son.height_calculator()
                        self.do_right_rotation(node, grandson)
                        node.height_calculator()
                        son.height_calculator()
                        grandson.height_calculator()
                        return 2
                if n_bf < 0 and s_bf > 0:
                        grandson = son.get_left()
                        self.do_right_rotation(son, grandson)
                        grandson.height_calculator()
                        son.height_calculator()
                        self.do_left_rotation(node, grandson)
                        node.height_calculator()
                        son.height_calculator()
                        grandson.height_calculator()
                        return 2
                return 0

        """ find the successor of node 
        @pre : node in self 
        @rtype: AVL node
        @returns: the successor of node
        """
        def successor (self,node) :
                if node.get_right().is_real_node():
                        return self.Min(node.get_right())
                temp = node.get_parent()
                while temp is not None and node == temp.right :
                        node = temp
                        temp = node.get_parent()
                return temp

        """ find the min 
        @pre: node is in self
        @returns : the node with the min key in node path 
        @:rtype AVL node
        """
        def Min(self,node):
                temp = node
                while temp.get_left().is_real_node() :
                        temp = temp.get_left()
                return temp

        """deletes node from the dictionary

        @type node: AVLNode
        @pre: node is a real pointer to a node in self
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
        def delete(self, node):
                return self.delete_node(node)

        """ deleting node as usual in BST and fixing size 
        @pre : node is in self 
        @rtype : int 
        @returns :  the number of rebalancing operation due to AVL rebalancing
        """
        def delete_node(self,node):
                flag= False
                node_parent = node.get_parent()
                node_right = node.get_right()
                node_left = node.get_left()
                virtual_Node = AVLNode(None, None)
                if not node_right.is_real_node() and not node_left.is_real_node() :
                        if node_parent is None:
                                self.root = virtual_Node
                        else : # node is not a root
                                if node_parent.get_left() == node :
                                        node_parent.set_left(virtual_Node)
                                else :
                                        node_parent.set_right(virtual_Node)
                elif not node_right.is_real_node() and node_left.is_real_node() : # case 2 : ond child
                        if node_parent is None:  # Root node
                                self.root = node_left
                        elif node_parent.get_left() == node:
                                node_parent.set_left(node_left)
                                node_left.set_parent(node_parent)
                        else:
                                node_parent.set_right(node_left)
                elif node_right.is_real_node() and not node_left.is_real_node() : # just bypass it , note that we didnt use set functions implemented in AVLnode class because there we add 1 to height
                        if node_parent is None:  # Root node
                                self.root = node_right
                        elif node_parent.left == node:
                                node_parent.left = node_right
                                virtual_Node.set_parent(node_parent)
                        else:
                                node_parent.right = node_right
                                virtual_Node.set_parent(node_parent)
                else : # case 2 : two children
                        successor_node = self.successor(node)  # Find the successor node
                        successor_node_parent = successor_node.get_parent()
                        node.set_value(successor_node.get_value())
                        node.set_key(successor_node.get_key())
                        if successor_node_parent.left == successor_node:
                                successor_node_parent.set_left(successor_node.right)
                                if successor_node.right.is_real_node():
                                        successor_node.right.set_parent(successor_node_parent)
                        else:
                                successor_node_parent.set_right(successor_node.right)
                                if successor_node.right.is_real_node():
                                        successor_node.right.set_parent(successor_node_parent)
                        self.size_count = self.size_count - 1  # update size
                        return self.Delete_Balance(successor_node_parent)

                self.size_count = self.size_count - 1  # update size
                return self.Delete_Balance(node_parent)


        """returns an array representing dictionary 

        @rtype: list
        @returns: a sorted list according to key of touples (key, value) representing the data structure
        """
        def avl_to_array(self):
                arr = []
                def avl_to_array_helper(node,arr):
                        if not node.is_real_node() :
                                return
                        avl_to_array_helper(node.left,arr)
                        arr.append((node.get_key(),node.get_value()))
                        avl_to_array_helper(node.right, arr)

                avl_to_array_helper(self.root,arr)
                return arr


        """returns the number of items in dictionary 

        @rtype: int
        @returns: the number of items in dictionary 
        """
        def size(self): # Simply return size field
                return self.size_count


        """splits the dictionary at the i'th index

        @type node: AVLNode
        @pre: node is in self
        @param node: The intended node in the dictionary according to whom we split
        @rtype: list
        @returns: a list [left, right], where left is an AVLTree representing the keys in the 
        dictionary smaller than node.key, right is an AVLTree representing the keys in the 
        dictionary larger than node.key.
        """

        def split(self, node):
                right_tree = AVLTree()
                left_tree = AVLTree()
                current = node
                left_tree.root=current.get_left()
                right_tree.root=current.get_right()
                while current.parent is not None :
                        if current == current.parent.right :
                                _leftSubtree = AVLTree()
                                _leftSubtree.root= current.parent.get_left()
                                left_tree.join(_leftSubtree, current.parent.get_key(), current.parent.get_value())
                        else :
                                _rightSubtree = AVLTree()
                                _rightSubtree.root = current.parent.get_right()
                                right_tree.join(_rightSubtree, current.parent.get_key(),current.parent.get_value())
                        current=current.get_parent()
                return [left_tree, right_tree]

        """joins self with key and another AVLTree
        @type tree2: AVLTree 
        @param tree2: a dictionary to be joined with self
        @type key: int 
        @param key: The key separting self with tree2
        @type val: any 
        @param val: The value attached to key
        @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        """

        def join(self, tree2, key, val):

                if self.root.height==-1 : #virtuals handiling
                        t2_height = tree2.root.height
                        if tree2.root.get_height() == -1 :
                                self.insert(key, val)
                                return 0
                        else :
                                tree2.root.parent = None
                                tree2.insert(key,val)
                                self.root=tree2.root
                                return t2_height +1
                if tree2.root.height == -1 : # if both virtuals , the case handeled above
                        self.insert(key,val) #self is not empty , just insert
                        return self.root.height # we dont add 1 because we inserted already

                x = AVLNode(key, val)
                x.set_height(0)
                t1_h = self.root.get_height()
                t2_h = tree2.root.get_height()
                t1_k = self.root.get_key()
                t2_k = tree2.root.get_key()
                if (t1_h == t2_h) and (t1_k < t2_k):
                        x.set_left(self.root)
                        x.set_right(tree2.root)
                        x.set_height(t1_h + 1)
                        self.root = x

                elif (t1_h == t2_h) and (t1_k > t2_k):
                        x.set_right(self.root)
                        x.set_left(tree2.root)
                        x.set_height(t1_h + 1)
                        self.root = x

                elif (t1_h < t2_h) and (t1_k < t2_k):
                        t1 = self
                        t2 = tree2
                        self.add(t1, t2, x, True)  # the boolean tells if the heigher tree`s keys are bigger than key

                elif (t1_h > t2_h) and (t1_k > t2_k):
                        t1 = tree2
                        t2 = self
                        self.add(t1, t2, x, True)

                elif (t1_h > t2_h) and (t1_k < t2_k):
                        t1 = tree2
                        t2 = self
                        self.add(t1, t2, x, False)

                elif (t1_h < t2_h) and (t1_k > t2_k):
                        t1 = self
                        t2 = tree2
                        self.add(t1, t2, x, False)

                self.size_count = self.size_count + tree2.size_count + 1
                return abs(t1_h - t2_h) + 1

        def add(self, t1, t2, x, add_to_left):
                t1_h = t1.root.get_height()
                t2_h = t2.root.get_height()

                needed = t2.root
                for h in range(t2_h):

                        if add_to_left:
                                needed = needed.get_left()  # node with the height of t1 at most
                        else:
                                needed = needed.get_right()

                        if needed.get_height() <= t1_h:
                                c = needed.get_parent()

                                if add_to_left:
                                        x.set_left(t1.root)
                                        x.set_right(needed)
                                        c.set_left(x)
                                        x.set_parent(c)
                                else:
                                        x.set_right(t1.root)
                                        x.set_left(needed)
                                        c.set_right(x)
                                        x.set_parent(c)

                                self.root = t2.get_root()
                                self.Delete_Balance(x)
                                return
        def get_root(self): # return root field , root is updated in the proccess
                return self.root






