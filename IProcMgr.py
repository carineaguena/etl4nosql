

class IProcMgt(object):
    
    def __init__(self, codOp, listOp):
        self.codOp = codOp
        self.listOp = listOp
    
    def process(self):
        return self.listOp
    
    def processParallel(self):
        pass
    
    def processDistributed(self):
        pass
    
    def processHybrid(self):
        pass