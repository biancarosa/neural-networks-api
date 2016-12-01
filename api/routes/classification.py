from api import app
from api.helpers.json_response_builder import JSONResponseBuilder
from api.models import ClassifierNetwork
from flask import request

@app.route('/classification/predict', methods=['POST'])
def classification():
    post_data = request.get_json()

    if post_data.get('entries'):
        if not post_data.get('network_id'):
            classifier_network = ClassifierNetwork()
            classifier_network.create()
        else:
            classifier_network = ClassifierNetwork.get(post_data['network_id'])
            if classifier_network is None:
                return JSONResponseBuilder.build_response(
                    success=False,
                    messages=['Network not found']
                ), 404
        predictions = classifier_network.predict(post_data['entries'])
        classifier_network.save()
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
