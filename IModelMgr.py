'''
Created on 3 de nov de 2017

@author: carineaguena

'''

# A variavel codFonte necessita do codigo da fonte dos dados que serao 
# utilizados na leitura ou criacao de procedimentos
class IModelMgt(object):
    
    def __init__(self, codFonte):
        self.codFonte = codFonte
        
    def readData(self):
        query_read = raw_input("Query to read:")
        return query_read
    
    def createOp(self):
        query_op = raw_input("Query to operate:")
        return query_op    
            
    
    
        