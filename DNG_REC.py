#!/usr/bin/env python
# coding: utf-8

# In[24]:
def recogn_domen(domen,t):
    return t.predict(data_prep_pred([domen]))


from turn_into_vector import words_into_vector
import pandas as pd
import joblib
from predictions import data_prep_pred
def recogn_file(name,t):
    data=pd.read_csv(name)
    data=data.values.tolist()
    domens = []
    for doman in data:
        domens.append(t.predict(data_prep_pred(doman)))
    return(domens)
    
from predictions import get_predictions
from predictions import data_prep_pred
from Data_prep import Data_Prep
from sklearn.neural_network import MLPClassifier
import numpy as np
from turn_into_vector import words_into_vector
from get_data import get_data
from estv import estv
t=MLPClassifier((20)*100, random_state=1,activation='logistic',max_iter=3000,warm_start=True)
y=np.array([0])
x=np.array([0]*38).reshape(1,-1)
t = joblib.load("model.pkl")
t.score(x, y)


print('Введите путь к файлу(csv) или домен')
inp=input()
if(inp[-4:]=='.csv'):
    result = recogn_file(inp,t)
    for res in result:
        if res == 0:
            print('dga')
        else:
            print('legit')
else:
    result = recogn_domen(inp,t)
    if result==0:
        print('dga')
    else:
        print('legit')
