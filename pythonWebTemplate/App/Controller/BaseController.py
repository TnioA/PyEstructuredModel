from flask import jsonify

class BaseController():
    def __init__(self):
        self
    
    def JsonResponse(obj):
        return jsonify(obj.__dict__)
    
    
