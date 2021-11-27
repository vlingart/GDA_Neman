#!/usr/bin/env python
# coding: utf-8

# In[24]:
def recogn_domen(domen,t):
    return t.predict(data_prep_pred([domen]))

from turn_into_vector import words_into_vector
import pandas as pd
from predictions import 
def recogn_file(name):
    data=pd.read_csv(name)
    data=data.tolist()
    data_prep_pred(data)
    t.predict(data)
    
from predictions import get_predictions
from predictions import data_prep_pred
from Data_prep import Data_Prep
from sklearn.neural_network import MLPClassifier
import numpy as np
from turn_into_vector import words_into_vector
from get_data import get_data
from estv import estv
t=MLPClassifier((20)*100, random_state=1,activation='logistic',max_iter=3000,warm_start=True)
y=np.array([0]).reshape(1,-1)
x=np.array([0]*36).reshape(1,-1)
t.fit(x,y)
with open('weights.txt','r') as r:
    for i in range(len(t.coefs_)):
        for j in range(len(t.coefs_[i])):
            for l in range(len(t.coefs_[i][j])): 
                t.coefs_[i][j][l]=r.readline()
print('Введите путь к файлу(csv) или домен')
inp=input()
if(inp[-4:]=='.csv'):
    recogn_file(inp,t)
else:
    recogn_domen(inp,t)

