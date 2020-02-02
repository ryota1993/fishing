#apis.py
######  Flask related Libraries   ############
from flask_restplus import Api

######  Import all .py API files  ########
from Login.login import api as login_api
from Test.test import api as test_api

#########  Adding Auth and all the APIs to Main   #################
authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}


api = Api(title = "TB Mapping APIs",
          description = "All the APIs for login and prediction",
         security='Bearer Auth', authorizations=authorizations)

### Login API ###
api.add_namespace(login_api, path="/login")
api.add_namespace(test_api, path="/test")
