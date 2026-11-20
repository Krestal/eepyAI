from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn import svm, ensemble
from sklearn.neural_network import MLPClassifier
import numpy as np

class ModelTrainer:
    # klasa do trenowania wielu modeli jednocześnie
    def __init__(self):
        self.models = {
            "DummyMean":   DummyRegressor(strategy="mean"),
            "LinearRegression":  LinearRegression(),
        }

    # trenowanie wszystkich modeli
    def train(self, X_train, y_train):
        self.trained_models = {}
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            self.trained_models[name] = model

    # predykcje dla wszystkich modeli; zmęczenie ma skalę 1-10, więc przycinamy wyniki
    def predict(self, X_test, clip_range=(1, 10)):
        predictions = {}
        for name, model in self.trained_models.items():
            y_pred = model.predict(X_test)
            if clip_range is not None:
                y_pred = np.clip(y_pred, *clip_range)
            predictions[name] = y_pred
        return predictions
