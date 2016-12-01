import pickle
from sklearn.neural_network import MLPClassifier
from api import db


class ClassifierNetwork(db.Document):

    pickled = db.BinaryField()

    def create(self):
        self.X = [[0., 0., 0.], [1., 1., 1.]]
        self.y = [0, 1]
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                hidden_layer_sizes=(5, 3), random_state=1)
        self.clf.fit(self.X, self.y)
        self.pickled = pickle.dumps(self.clf)

    @staticmethod
    def get(network_id):
        classifier_network = ClassifierNetwork.objects(id=network_id).first()
        classifier_network.clf = pickle.loads(classifier_network.pickled)
        return classifier_network

    def predict(self, entries):
        predictions = self.clf.predict(entries)
        self.pickled = pickle.dumps(self.clf)
        return predictions.tolist()
