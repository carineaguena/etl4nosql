'''
Created on 3 de nov de 2017

@author: carineaguena
'''
from __builtin__ import raw_input

class IDataMgt(object):
     
    def __init__(self, host, user, password):
        self.host=host
        self.user=user
        self.password=password
        
    def connection(self):
        query = raw_input("Query to connect:")
        return query
        
    def structureType(self):
        sttype = raw_input("Database type:")
        return sttype 
    
    def allowWrite(self):
        pass