import sys

class EulerPhi:

    def __init__(self, number):
        self.number = number
    
    ## Factorize with primes
    def factorize(self):
        ## Check if prime
        def is_prime(n):
            if n in (1,2):
                return True
            for ix in range(2,int(n**(1/2))+1):
                if n%ix==0:
                    return False
            return True

        store = dict()
        ix = 2
        
        remainder = self.number
        while remainder and not is_prime(remainder):
            n = 1
            while remainder%(ix**n) == 0:
                n+=1
            store.update({ix: n-1})
            remainder /= (ix**store[ix])
            ix+=1
            while not is_prime(ix):
                ix+=1
        if remainder:
            store.update({int(remainder): 1})
        return store
    
    def phi_(self, factors):

        self.phi = 1
        ps = sorted(factors.keys())
        es = tuple(factors[i] for i in ps)
        gen = (ps[i]**(es[i])-ps[i]**(es[i]-1) for i in range(0,len(factors)))

        while True:
            try:
                self.phi*=next(gen)
            except StopIteration:
                return
        
    def main(self):
        self.phi_(self.factorize())
        return self.phi


if __name__ == '__main__':

    euler = EulerPhi(int(sys.argv[1]))
    euler.main()
    sys.exit(str(euler.phi))




