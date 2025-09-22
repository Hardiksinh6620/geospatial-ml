"""Land-cover classification helper."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_classifier(X, y, n_estimators=100, test_size=0.2, random_state=42):
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=test_size,
                                          random_state=random_state,
                                          stratify=y)
    clf = RandomForestClassifier(n_estimators=n_estimators,
                                 random_state=random_state)
    clf.fit(Xtr, ytr)
    pred = clf.predict(Xte)
    return clf, {"accuracy": float(accuracy_score(yte, pred))}
