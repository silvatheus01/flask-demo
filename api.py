from flask import Flask, request
from flask_restful import Resource, Api, abort
from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests
from unidecode import unidecode 

app = Flask(__name__)
api = Api(app)

class Age(Resource):
    def post(self):
        data = request.get_json()

        if(not 'name' in data):
            abort(400, message='O campo "name" não foi encontrado no body da requisição.')
        if(not 'birthdate' in data):
            abort(400, message='O campo "birthdate" não foi encontrado no body da requisição.')
        if(not 'date' in data):
            abort(400, message='O campo "date" não foi encontrado no body da requisição.')        
        
        birthdate = data['birthdate']
        date = data['date']
        
        try:
            future = datetime.strptime(date, '%Y-%m-%d')
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        except ValueError as err:
            abort(422, message=str(err))

        today = datetime.today()

        years_old_today = relativedelta(today, birthdate).years
        years_old_future = relativedelta(future, birthdate).years

        if(today < birthdate):
            abort(422, message='A data do campo "birthdate" é futura.')
        if(future < birthdate):
            abort(422, message='A data do campo "date" deve ser maior do que a data do campo "birthdate".')
        if(future < today):
            abort(422, message='A data do campo "date" deve ser futura.')

        name = data['name']

        quote = "Olá, {}! Você tem {} anos e em {} você terá {} anos.".format(name, years_old_today, future.strftime("%d/%m/%Y"), years_old_future)
        age_now = years_old_today
        ageThen = years_old_future        

        return {"quote": quote, "ageNow": age_now, "ageThen": ageThen}

class Municipio(Resource):
    def get(self):
        municipio = request.args.get('municipio')
        if(not municipio):
            abort(400, message='O parâmetro "municipio" é obrigatório.')

        formatted_municipio = unidecode(municipio.replace(" ", "-"))
        response = requests.get('http://servicodados.ibge.gov.br/api/v1/localidades/municipios/{}'.format(formatted_municipio))
        status_code = response.status_code

        if(status_code != 200):
            abort(503, message="Não foi possível acessar o recurso requisitado.")

        data = response.json()
        if(len(data) == 0):
            abort(404, message='O município requisitado não foi encontrado.')

        id = data.get('id')
        response = requests.get('http://servicodados.ibge.gov.br/api/v1/localidades/municipios/{}/subdistritos'.format(id))
        data = response.json()

        bairros = []
        for bairro in data:
            bairros.append(bairro.get("nome"))

        return {"municipio": municipio, "bairros": bairros}

api.add_resource(Age, '/age')
api.add_resource(Municipio, '/municipio-bairros')

if __name__ == '__main__':
    app.run(debug=True)