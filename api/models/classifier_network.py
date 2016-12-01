from sklearn.neural_network import MLPClassifier

class ClassifierNetwork(object):

    def __init__(self):
        self.X = [[0., 0., 0.], [1., 1., 1.]]
        self.y = [0, 1]
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                hidden_layer_sizes=(5, 3), random_state=1)
        self.clf.fit(self.X, self.y)

    def predict(self, entries):
        predictions = self.clf.predict(entries)
        return predictions.tolist()
