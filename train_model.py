from germansentiment import SentimentModel

model = SentimentModel()

import pickle
with open('./model.pkl', 'wb') as model_pkl:
    pickle.dump(model, model_pkl)

    