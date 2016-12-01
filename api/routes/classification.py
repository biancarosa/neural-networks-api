import json
from sklearn.neural_network import MLPClassifier
from api import app

@app.route('/classification')
def classification():
    X = [[0., 0., 0.], [1., 1., 1.]]
    y = [0, 1]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
            hidden_layer_sizes=(5, 3), random_state=1)
    clf.fit(X, y)
    predictions = clf.predict([[2., 2., 3.], [-1., -2., -2.]])
    response = { 'data' : [], 'success': False }
    response['data'] = predictions.tolist()
    response['success'] = True
    data = json.dumps(response, indent=2)
    return data
