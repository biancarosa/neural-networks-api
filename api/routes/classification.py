from api import app
from api.helpers.json_response_builder import JSONResponseBuilder
from api.models import ClassifierNetwork

@app.route('/classification')
def classification():
    classifier_network = ClassifierNetwork()
    predictions = classifier_network.predict([[1.,1.,1.], [0.,0.,0.]])
    return JSONResponseBuilder.build_response(data=predictions)
