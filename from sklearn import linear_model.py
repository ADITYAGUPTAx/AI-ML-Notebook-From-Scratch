from sklearn import linear_model
import pickle

with open("model_pickle",'rb') as f:
    model = pickle.load(f)

model.coef_