
# Login/json_checker.py
#################   Flask related Libraries   ###########################
from flask import request,json,jsonify,make_response

################# Login Route ###################
class json_checker():
    
    def __init__(self):
        pass
    
    def check(self,request): #Check if API request for login is valid
        
        if not request.is_json:
            return {"msg": "Missing JSON in request"},400
        
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        
        if not username:
            return {"msg": "Missing username parameter"},400
        if not password:
            return {"msg": "Missing password parameter"},400
        
        # TODO: Change authentication logic using LDAP
        if username != 'test' or password != 'test':
            return {"msg": "Not authenticated user"},401
        
        return username,password

    