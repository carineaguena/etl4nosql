

class IModelMgt(object):
    
    def __init__(self, codDB):
        self.codDB = codDB
        
    def readData(self):
        query_read = raw_input("Query to read:")
        return query_read
    
    def createOp(self):
        query_op = raw_input("Query to operate:")
        return query_op    
            
    def writeData(self):
        query_write = raw_input("Query to write:")
        return query_write
        
        
