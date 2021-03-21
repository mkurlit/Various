import sys

class TreeNode:

    def __init__(self, r_val, q, left = None, right = None, parent = None):
        self.r_val = r_val
        self.q = q
        self.left = left
        self.right = right
        self.parent = parent
    
    def is_leaf(self):
        return not (self.left or self.right)
    
    def add_children_from_dct(self, children):

        left_ch = max(children.keys())
        self.left = TreeNode(left_ch, children[left_ch], parent = self)

        right_ch = min(children.keys())
        self.right = TreeNode(right_ch, children[right_ch], parent = self)

    def get_level(self):
        l = 0
        p = self.parent
        while p:
            l+=1
            p = p.parent
        
        return l
    
    def get_leaves(self):
        leaves = list()
        def _get_leaves(node):
            if node:
                if node.is_leaf():
                    leaves.append(node)
                if node.left:
                    _get_leaves(node.left)
                if node.right:
                    _get_leaves(node.right)
        _get_leaves(self)
        return leaves

    def print(self):
        print(f'{" "*5*self.get_level()}-> (r={self.r_val}, q={self.q})')
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()





