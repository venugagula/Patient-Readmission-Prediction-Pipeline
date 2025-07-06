import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model():
    df = pd.read_parquet("data/model_ready.parquet")
    X = df.drop("readmitted", axis=1)
    y = df["readmitted"]

    smote = SMOTE()
    X_res, y_res = smote.fit_resample(X, y)

    X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

    joblib.dump(model, "model/readmission_model.pkl")

if __name__ == "__main__":
    train_model()

