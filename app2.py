from flask import Flask, jsonify

from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)
app.json = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title' : LazyString(lambda: 'API Documentation for Data Processing and Modelling'),
        'version' : LazyString(lambda: '1.0.0'),
        'description' : LazyString(lambda: 'API Documentation untuk Data Processing dan Modelling'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json',
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "spec_route": "/docs/"
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)
@swag_from("docs/example.yml", methods=['GET'])

@app.route('/docs/', methods=['GET'])
def example():
    data = {
        'status_code': 200,
        'description': 'Success',
        'data': {
            'message': 'Ini contoh data',
            'value': 42
        }
    }
    response = jsonify(data)
    return response
        
if __name__ == '__main__':
    app.run()