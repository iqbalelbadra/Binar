from flask import Flask, jsonify, request
from data_prep import create_json_response

from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)
app.json = LazyJSONEncoder
swagger_template = {'info':{'title': LazyString(lambda: 'API Documentation for Data Processing dan Modelling'),
                            'version': LazyString(lambda: '1.0.0'),
                            'description': LazyString(lambda : 'Dokumnetasi API untuk Data Processing dan Modelling')
                            },
                    'host':LazyString(lambda: request.host)
                    }
swagger_config = {
    "headers": [],
    "specs": [{"endpoint": 'docs',"route": '/docs.json',}],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "spec_route": "/docs/"
}

swagger = Swagger(app,
				  template = swagger_template,
				  config = swagger_config
				 )

@swag_from("docs/example.yml", methods=['GET'])
@app.route('/', methods=['GET'])
def example():
    json_response = create_json_response(description="Ini teks awal",
                                         message="Cuma message")
    response = jsonify(json_response)
    response.headers.add('Content-Type', 'application/json')
    return response


@app.route('/dua', methods=['GET'])
def another():
    json_response = create_json_response(description="Ini teks kedua",
                                         message="Pake routing")
    response = jsonify(json_response)
    response.headers.add('Content-Type', 'application/json')
    return response

@app.route('/tiga', methods=['GET'])
def third():
    data = {
        'status_code': 200,
        'description': 'Third endpoint',
        'data': {
            'message': 'Ini data ketiga',
            'value': 999
        }
    }
    response = jsonify(data)
    response.headers.add('Content-Type', 'application/json')
    return response

if __name__ == '__main__':
    app.run(debug=True)
