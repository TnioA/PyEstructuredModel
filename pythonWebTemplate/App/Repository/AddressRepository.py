import requests
import json

class AddressRepository:
    
    def __init__(self):
        pass
    
    def GetAddress(self, zipCode):
        content = json.loads(requests.get("http://viacep.com.br/ws/" + zipCode + "/json/").text)
        return content