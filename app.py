import re
import pandas as pd
import sqlite3

from flask import Flask, jsonify, request, redirect
from data_cleansing import processing_text,processing_word
from data_wnr import create_table,insert_to_table,read_table

from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

# create flask object
app = Flask(__name__)
app.json_provider_class	 = LazyJSONEncoder


title = str(LazyString(lambda: 'API Documentation for Data Processing dan Modelling'))
version = str(LazyString(lambda: '1.0.0'))
description = str(LazyString(lambda : 'Dokumnetasi API untuk Data Processing dan Modelling'))
host = LazyString(lambda: request.host)

# create swagger_template
# swagger_template = {'info':{'title': title,
#                            'version': version,
#                            'description': description 
#                            },
#                    'host': host
#                    }

swagger_config = {
	"headers": [],
	"specs": [{"endpoint":"docs", "route": '/docs.json'}],
	"static_url_path": "/flasgger_static",
	"swagger_ui":True,
	"specs_route":"/docs/"
}
swagger_config["info"] = {
    "title": "API Documentation for Data Processing",
    "version": "1.0.0",
    "description": "This API provides text data cleaning capabilities for Bahasa Indonesia. It performs cleaning operations on text data, including the removal of abusive words and slang (alay) words."
}

swagger = Swagger(app,
#				  template = swagger_template,
				  config = swagger_config
				 )



@app.route('/', methods= ['GET'])
def hello():
	return redirect('/docs/')

# @swag_from("docs/text-processing.yml", methods=['POST'])
# @app.route('/text-processing',methods=['POST'])
# def text_processing():

# 	df = pd.read_csv('Asset/data.csv', encoding='latin1')
# 	cleaned_text = re.sub(r'[^a-zA-Z0-9]',' ', text)
	
# 	json_response = create_json_response(description="Teks yang sudah di proses", 
# 				      					 data=cleaned_text)
	
# 	response_data = jsonify(json_response)
# 	return response_data

@swag_from("docs/input_processing.yml", methods=['POST'])
@app.route('/input-processing',methods=['POST'])
def input_processing():
    text = request.form.get('text')
    cleaned_tweet = processing_text(text)
    cleaned_tweet = processing_word(cleaned_tweet)
    #results = read_table(table_name='tweet_cleaning')
    #last_index = len(results)
    insert_to_table(text, cleaned_tweet)
    
    json_response = {'Status':'Success Cleaned and Insert to Table',
                    'Previous Tweet':text,
                    'Cleaned Tweet':cleaned_tweet,
                    }
    response_data = jsonify(json_response)

    return response_data

# @swag_from("docs/file_processing.yml", methods=['POST'])
# @app.route('/file-processing',methods=['POST'])
# def file_processing():
    
#     df = pd.read_csv('Asset/data.csv', encoding='latin1')
#     create_table() 
#     for ori, tweet in enumerate(df['Tweet']):
#         ori = tweet 
#         cleaned_tweet = processing_text(tweet)
#         cleaned_tweet = processing_word(cleaned_tweet)		
#         insert_to_table(ori, cleaned_tweet)
    
#     response_data = jsonify('response:"SUCCESS"')
#     return response_data
@swag_from("docs/file_processing.yml", methods=['POST'])
@app.route('/file-processing', methods=['POST'])
def file_processing():
    file = request.files['file']
    if file:
        df = pd.read_csv(file, encoding='latin1')
        if("Tweet" in df.columns):
            create_table()
            for idx, row in df.iterrows():
                previous_tweet = row['Tweet']
                cleaned_tweet = processing_text(previous_tweet)
                cleaned_tweet = processing_word(cleaned_tweet)
                insert_to_table(previous_tweet, cleaned_tweet)

            response_data = jsonify({'response': 'SUCCESS'})
            return response_data
        else:
            response_data = jsonify({'ERROR_WARNING': "No COLUMNS Tweet APPEAR ON THE UPLOADED FILE"})
            return response_data
    else:
        response_data = jsonify({'response': 'No file uploaded'})
        return response_data


@swag_from("docs/read_index_data.yml", methods=['POST'])
@app.route('/read-index-data',methods=['POST'])
def read_index_data():
    index = request.form.get('index')
    
    results = read_table(target_index=int(index),table_name='tweet_cleaning')
    previous_tweet = results[0]
    cleaned_tweet = results[1]
    json_response = {'Index':index,
                    'Previous Tweet':previous_tweet,
                    'Cleaned Tweet':cleaned_tweet,
                    }
    response_data = jsonify(json_response)
    return response_data

if __name__ == '__main__':
	app.run(debug=True)
