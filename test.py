import pickle

with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
texts = [
    "Mit keinem guten Ergebniss"]
result = model.predict_sentiment(texts)
print(result)