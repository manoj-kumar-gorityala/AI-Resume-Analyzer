import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# load dataset
data = pd.read_csv("dataset.csv")

X = data["Resume"]
y = data["Role"]

# TF-IDF
vectorizer = TfidfVectorizer(stop_words="english")

X_vector = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()

model.fit(X_vector, y)

# save model
pickle.dump(model, open("model.pkl","wb"))
pickle.dump(vectorizer, open("vectorizer.pkl","wb"))

print("Model trained successfully")