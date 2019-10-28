from Oportunidades import Oportunidade
from flask import Flask
from flask_restful import Api, Resource
import json

# FLASK_APP=endpoints.py FLASK_DEBUG=1 python -m flask run

app = Flask(__name__)
api = Api(app)

def default(obj):
    if hasattr(obj, "__json__"):
        return obj.__json__()
    return json.JSONEncoder.default(obj)

class HealthCheck(Resource):

    def get(self):
        return 200

class OptAPI(Resource):
    def get(self,id):
        with open("lista_oportunidades.json", "r") as jsonFile:
            data = json.load(jsonFile)
        return data[str(id)], 200

    def put(self, id):
        with open("lista_oportunidades.json", "r") as jsonFile:
            data = json.load(jsonFile)
        
        if data[str(id)]["ativo"] == True:
            data[str(id)]["ativo"] = False
        else:
            data[str(id)]["ativo"] = True

        with open("lista_oportunidades.json", "w") as jsonFile:
            json.dump(data, jsonFile)        

    def delete(self, id):
        with open("lista_oportunidades.json", "r") as jsonFile:
            data = json.load(jsonFile)  
        
        del data[str(id)]
        
        with open("lista_oportunidades.json", "w") as jsonFile:
            json.dump(data, jsonFile)  

class OptsAPI(Resource):
        
        def get(self):
            with open("lista_oportunidades.json", "r") as jsonFile:
                data = json.load(jsonFile)

            return data, 200

        def post(self):
            with open("lista_oportunidades.json", "r") as jsonFile:
                data = json.load(jsonFile)
            id = len(data)
            new_opt = Oportunidade("Férias","Insper","Cloud","2K",True)
            data[id] = new_opt.dict
            with open("lista_oportunidades.json", "w") as jsonFile:
                json.dump(data, jsonFile)  





api.add_resource(OptAPI, '/opt/<int:id>', endpoint = 'opt')
api.add_resource(OptsAPI, '/opts', endpoint = 'opts')
api.add_resource(HealthCheck, '/healthcheck', endpoint = 'healthcheck')