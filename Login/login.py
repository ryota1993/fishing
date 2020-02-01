
#Login/login.py
#################   Flask related Libraries   ###########################
from flask import request,json,jsonify,make_response
from flask_restplus import Namespace, Resource, fields
from flask_jwt_extended import create_access_token

##############   Import Classes   ###################
from Login.json_checker import json_checker
json_checker = json_checker()

############################# Login API ###########################
api = Namespace('Login', description='Login-related APIs')

login_json = api.model('login_json', {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password'),
})

#################### Login Route ######################
@api.route('', methods=['POST'])
@api.doc(security=None)
class Login(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Missing or Invalid Argument', 401: 'User not authenticated' })
    @api.expect(login_json)
    def post(self):

        if isinstance(json_checker.check(request)[0],dict):
            error_msg = json_checker.check(request)[0]
            http_status_code = json_checker.check(request)[1]

            return make_response(jsonify(error_msg),http_status_code)

        #If successfully authenticated
        username,password = json_checker.check(request)

        # Identity can be any data that is json serializable
        return make_response(jsonify(user={
                "token": create_access_token(identity=username),
                "username": username
            }), 200)
