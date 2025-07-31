import pickle
from sklearn.linear_model import LinearRegression
with open('model.pickle','rb') as f:
    model=pickle.load(f)

model

