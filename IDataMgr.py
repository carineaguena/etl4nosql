
from __builtin__ import raw_input
import os

class IDataMgt(object):
    host = None
    user = None
    password = None
    query_con = None
    sttype = None
     
    def __init__(self):
        pass 
        
    def connection(self):
        query = raw_input("Query to connect:")
        self.query_con = query
        return query
        
    def structureType(self):
        sttype = raw_input("Database type:")
        self.sttype = sttype
        return sttype 
    
    def allowWrite(self):
        pass
    
    def connectMongo(self):
        os.system("/Users/carineaguena/Documents/mongodb/bin/mongod --dbpath /Users/carineaguena/Documents/data/db/")
        return

    def clientMongo(self):
        os.system("/Users/carineaguena/Documents/mongodb/bin/mongo")
        return

#t = threading.Thread(target=connectMongo())
#t2 = threading.Thread(target=clientMongo())
#t.start()
#t2.start()