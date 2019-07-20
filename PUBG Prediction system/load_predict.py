import pandas as pd 
import numpy as np 
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.models import load_model

load_path = "model/pubg_model100epochs.h5"

def load():
    model = load_model(load_path)
    print(model.summary())
    return model

def predict_res(data,model):
    pred = model.predict(data.values)
    res = np.mean(pred)
    return res
    