#!/usr/bin/env python
# coding: utf-8

# In[14]:


from predictions import get_predictions
from predictions import data_prep_pred
from Data_prep import Data_Prep
from sklearn.neural_network import MLPClassifier
import numpy as np
from turn_into_vector import words_into_vector
from get_data import get_data
from estv import estv
Data_train,Data_valid=Data_Prep('dataset_clear.csv',purp='T')
t=MLPClassifier((20)*100, random_state=1,activation='logistic',max_iter=3000)
t.fit(Data_train[0],Data_train[1])
with open('weights.txt','w') as w:
    for i in range(len(t.coefs_)):
        for j in range(len(t.coefs_[i])):
            for l in range(len(t.coefs_[i][j])): 
                w.write(str(t.coefs_[i][j][l])+'\n')

