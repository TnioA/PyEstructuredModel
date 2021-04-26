import json

class UserRepository:
    
    def __init__(self, context):
        self.context = context
    
    def GetAll(self):
        self.context.Connect()
        
        self.context.Disconnect()
        
    def GetById(self, id):
        pass
        