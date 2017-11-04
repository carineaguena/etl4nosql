

class IOpMgt(object):
    def __init__(self, codModel):
        self.codModel = codModel
        self.ops = []
    
    def modelOperation(self):
        pass    
    
    def putOps(self, op):
        self.ops.append(op)
        
    def getOp(self, op):
        index = self.ops.index(op)
        return self.ops[index]
    
    def getOps(self):
        return self.ops
        
    def popOp(self, op):
        self.ops.pop(self.ops.index(op))
        