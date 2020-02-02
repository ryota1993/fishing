
#Test/test.py
#################   Flask related Libraries   ###########################
from flask import request,json,jsonify,make_response
from flask_restplus import Namespace, Resource, fields
from flask_jwt_extended import create_access_token

##############   Import Classes   ###################
from Login.json_checker import json_checker
json_checker = json_checker()

############################# Login API ###########################
api = Namespace('Test', description='Test APIs')

test_json = api.model('test_json', {
    'season': fields.Integer(required=True, description='season'),
})

#################### Login Route ######################
@api.route('', methods=['POST'])
@api.doc(security=None)
class Test(Resource):

    @api.doc(responses={ 200: 'OK', 400: 'Missing or Invalid Argument', 401: 'User not authenticated' })
    @api.expect(test_json)
    def post(self):

        test = request.get_json("season")
        return make_response(jsonify({"msg":"API request from Wrodpress received","received value":test}),200)
