import datetime
import joblib
from sklearn.ensemble import RandomForestClassifier


class Machine:

    def __init__(self, df):
        target = df['Rarity']
        features = df.drop(columns=['Rarity'])
        self.model = RandomForestClassifier(
            random_state=6,
            n_estimators=9,
            n_jobs=-1,
            max_depth=19
        )

        self.model.fit(features, target)
        self.timestamp = datetime.datetime.now()

    def __call__(self, feature_basis):
        prediction, *_ = self.model.predict(feature_basis)
        confidence, *_ = self.model.predict_proba(feature_basis)
        return prediction, max(confidence)

    def save(self, filepath):
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        return joblib.load(filepath)

    def info(self):
        name = self.model.__class__.__name__
        return f"Model: {name} <br> Timestamp: {self.timestamp}"
