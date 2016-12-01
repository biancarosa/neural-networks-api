from api import app
from api.helpers.json_response_builder import JSONResponseBuilder
from api.models import ClassifierNetwork
from flask import request

@app.route('/classification/predict', methods=['POST'])
def classification():
    post_data = request.get_json()

    if post_data.get('entries'):
        classifier_network = ClassifierNetwork()
        predictions = classifier_network.predict(post_data['entries'])
        return JSONResponseBuilder.build_response(
            data={
                "output" : predictions
            }
        ), 200
    else:
        return JSONResponseBuilder.build_response(
                success=False,
                messages=['Please send the entries to predict the output']
            ), 400
