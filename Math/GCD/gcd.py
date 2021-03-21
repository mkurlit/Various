from aux_tree import TreeNode

class GCD:

    """GCD calculator\n
    Euclidean Reduction Method"""

    def __init__(self, r0, r1, extended = False):
        self.r0 = max(r0, r1) 
        self.r1 = min(r0, r1)
        if not extended:
            self.gcd_path = self.get_gcd()
            self.gcd = self.gcd_path[-2]
        else:
            self.extended = self.get_extended()
            self.gcd = self.extended['gcd']

    ## Standard Reduction
    def get_gcd(self):
        
        store_path = [max(self.r1,self.r0),min(self.r0,self.r1)]

        while store_path[-1] > 0:
            rr0 = store_path[-2]
            rr1 = store_path[-1]
            store_path.append(rr0 % rr1)
        
        return store_path
    
    ## Extended
    def get_extended(self):

        store = {'r0': max(self.r0,self.r1),
                 'r1': min(self.r0, self.r1),
                 'r2': max(self.r0, self.r1) % min(self.r0, self.r1),}

        remainder = store['r2']
        ix = 3

        st = {store['r2']: {store['r0']: 1, store['r1']: -(store['r0']//store['r1'])}}

        while remainder>0:

            rr = store[f'r{ix-2}']%store[f'r{ix-1}']
            
            if rr > 0:
                store[f'r{ix}'] = rr
                st.update({rr: {store[f'r{ix-2}']: 1, 
                                store[f'r{ix-1}']: -(store[f'r{ix-2}']//store[f'r{ix-1}'])}})
            
            remainder = rr
            ix+=1

        gcd = min(st.keys())

        ## build a tree
        tree = TreeNode(gcd, 0)
        tree.add_children_from_dct(st[gcd])

        while any(n.r_val not in (self.r0, self.r1) for n in tree.get_leaves()):
            for n in tree.get_leaves():
                if n.r_val not in (self.r0, self.r1):
                    n.add_children_from_dct(st[n.r_val])
        
        leaves = tree.get_leaves()
        q0 = 0
        q1 = 0
        for n in leaves:
            counter = 1
            if n.r_val == self.r0:
                while n.parent:
                    counter*=n.q
                    n = n.parent
                q0+=counter
            elif n.r_val == self.r1:
                while n.parent:
                    counter*=n.q
                    n = n.parent
                q1+=counter

        return {'gcd': gcd,
                's': q0,
                'r0': self.r0,
                't': q1,
                'r1': self.r1}
