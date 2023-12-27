class sparseMatrix():
    def __init__(self):
        self.matrix = {}

    def add(self, name, pincode):
        if name in self.matrix:
            self.matrix[name].add(pincode)
        else:
            self.matrix[name] = {pincode}

    def addset(self, name, pincodes):
        self.matrix[name] = pincodes

    def check(self, name, pincode):
        return (name in self.matrix) and (pincode in self.matrix[name])
    
if __name__ == '__main__':
    import random
    import time
    import gc

    checks = int(1e7)
    nMerchants = int(1e7)
    nPincodes = int(40000)

    
    start = time.time()
    print('Creating pincodes list', end = '\r')
    pincodes = {id for id in range(nPincodes)}
    print('Pincodes list created', end = '\r')

    m = sparseMatrix()
    print('Adding Merchants and Pincodes', end = '\r')
    for merchant in range(nMerchants):
        m.addset(f'merchant{merchant}', pincodes)
    print('Matrix updates',end = '\r')
    print(f'Total Matrix Creation time = {time.time() - start}')

    print('Creating Checks',end = '\r')
    checklist = [(random.randint(0,2*nPincodes),f'merchant{random.randint(0, nMerchants)}') for i in range(checks)]
    print('Random Checks Created',end = '\r')
    print('Evaluation Started',end = '\r')


    start = time.time()
    for pincode, merchant in (checklist):
        (m.check(merchant, pincode))
    print('Evaluation Completed',end = '\r')
    print(f'No of checks: {checks}  | Check time = {time.time() - start}')

    print('Deleting Vars',end = '\r')
    del m
    del pincodes
    del checks
    gc.collect()
    print(' '*30,end='\r')
    print('Done', end='\r')

    print('Sparse Matrix [Merchants] : set(Pincodes)')
    