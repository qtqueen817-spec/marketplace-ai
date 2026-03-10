from sklearn.feature_extraction.text import TydfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample data to "train" our mini-model
data = [
    ("iPhone 13 pro max like new", "Electronics"),
    ("Wooden dining table with 4 chairs", "Furniture"),
    ("Gaming laptop RTX 3080", "Electronics"),
    ("Leather sofa brown color", "Furniture"),
    ("Nike running shoes size 10", "Fashion")
]

texts, labels = zip(*data)
vectorizer = TydfVectorizer()
classifier = MultinomialNB()

# Train the model
X = vectorizer.fit_transform(texts)
classifier.fit(X, labels)

def predict_category(description: str):
    X_new = vectorizer.transform([description])
    prediction = classifier.predict(X_new)
    return prediction[0]