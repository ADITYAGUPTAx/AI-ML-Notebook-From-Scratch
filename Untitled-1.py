import pickle
from sklearn import linear_model as lm
with open('model_pickle','rb') as f:
    model=pickle.load(f)

print(model.predict([[78]]))