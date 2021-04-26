from App.Repository.UserRepository import UserRepository
from App.Model.Context import Context

class UserController:
    def __init__(self):
        self.context = Context()
        self.repository = UserRepository(self.context)
        
    def GetAll(self):
        response = self.repository.GetAll()
        return response
    