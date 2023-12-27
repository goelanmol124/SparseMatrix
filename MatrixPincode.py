class sparseMatrix():
    def __init__(self):
        self.matrix = {}

    def add(self, pincode, name):
        if pincode in self.matrix:
            self.matrix[pincode].add(name)
        else:
            self.matrix[pincode] = {name}

    def addset(self, pincode, merchants):
        self.matrix[pincode] = merchants


    def check(self, pincode, name):
        return (pincode in self.matrix) and (name in self.matrix[pincode])
    
if __name__ == '__main__':
    import random
    import time
    import gc

    checks = int(1e7)
    nMerchants = int(1e7)
    nPincodes = int(40000)

    print('Sparse Matrix [Pincode] : set(Merchants)')

    start = time.time()
    print('Creating merchants list', end = '\r')
    merchants = {f'merchant{id}' for id in range(nMerchants)}
    print('Merchants list created', end = '\r')

    m = sparseMatrix()
    print('Adding Merchants and Pincodes', end = '\r')
    for pincode in range(nPincodes):
        m.addset(pincode, merchants)
    print('Matrix updates',end = '\r')
    print(f'Total Matrix Creation time = {time.time() - start}')

    print('Creating Checks',end = '\r')
    checklist = [(random.randint(0,2*nPincodes),f'merchant{random.randint(0, nMerchants)}') for i in range(checks)]
    print('Random Checks Created',end = '\r')
    print('Evaluation Started',end = '\r')


    start = time.time()
    for pincode, merchant in (checklist):
        (m.check(pincode, merchant))
    print('Evaluation Completed',end = '\r')
    print(f'No of checks: {checks}  | Check time = {time.time() - start}')

    print('Deleting Vars',end = '\r')
    del m
    del merchants
    del checks
    gc.collect()
    print(' '*30,end='\r')
    print('Done', end='\r')

    print('Sparse Matrix [Merchants] : set(Pincodes)')
    