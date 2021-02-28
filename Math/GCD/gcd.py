class GCD:

    """GCD calculator\n
    Euclidean Reduction Method"""

    def __init__(self, r0, r1):
        self.r0 = r0 
        self.r1 = r1
        self.gcd_path = self.get_gcd()
        self.gcd = self.gcd_path[-2]

    def get_gcd(self):
        
        store_path = [max(self.r1,self.r0),min(self.r0,self.r1)]

        while store_path[-1] > 0:
            rr0 = store_path[-2]
            rr1 = store_path[-1]
            store_path.append(rr0 % rr1)
        
        return store_path
