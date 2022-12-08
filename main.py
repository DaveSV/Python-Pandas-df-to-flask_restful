from flask import Flask, request, render_template, session, redirect
from flask_restful import Resource, Api
import numpy as np
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

df = pd.DataFrame({'Autor': ['Miguel de Cervantes', 'Lope de Vega', 'Francisco de Quevedo'],
                   'Cita1': ['Oh, memoria, enemiga mortal de mi descanso', 'Los celos son hijos del amor, mas son bastardos, te confieso', 'El que quiere de esta vida todas las cosas a su gusto, tendrá muchos disgustos'],
                   'Cita2': ['La virtud mas es perseguida de los malos que amada de los buenos', 'Que de una mujer que es buena mil cosas buenas se aprenden', 'Las palabras son como monedas, que una vale por muchas como muchas no valen por una']})

class Quotes(Resource):
    def get(self):
        return {
            'Don Quijote de la Mancha': {
                'cita1': ['Oh, memoria, enemiga mortal de mi descanso'],
                'cita2': ['La virtud mas es perseguida de los malos que amada de los buenos']
                
        },
        'Lope de Vega': {
            'cita1': ['Los celos son hijos del amor, mas son bastardos, te confieso'],
            'cita2': ['Que de una mujer que es buena mil cosas buenas se aprenden']
            },
        'Francisco de Quevedo': {
            'cita1': ['El que quiere de esta vida todas las cosas a su gusto, tendrá muchos disgustos'],
            'cita2': ['Las palabras son como monedas, que una vale por muchas como muchas no valen por una']
            }
        }

api.add_resource(Quotes, '/')

@app.route('/dataset', methods=("POST", "GET"))
def html_table():

    return render_template('dataset.html',  tables=[df.to_html(classes='data',  border=None)], titles=df.columns.values)


@app.route('/pd_to_json', methods=("POST", "GET"))
def to_json():

    jsonfiles = json.loads(df.to_json(orient='records'))

    return render_template('dataset.html', ctrsuccess=jsonfiles)


if __name__ == '__main__':
    app.run(debug=True)
