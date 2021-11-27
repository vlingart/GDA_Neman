#!/usr/bin/env python
# coding: utf-8

import numpy as np
from Data_prep import est_prep
from Data_prep import host_to_domain
from estv import estv 
from turn_into_vector import words_into_vector 
# In[ ]:


def get_predictions(vector,model1,model2,model3):
    Data_Chisl_to_pred=[]
    Data_dlin_to_pred=[]
    Data_est_to_pred=[]
    for i in range(len(vector)):
        Data_Chisl_to_pred.append(vector[i][0:36])
        Data_dlin_to_pred.append(vector[i][37])
        Data_est_to_pred.append(vector[i][36])
    Data_Chisl_to_pred=np.array(Data_Chisl_to_pred)
    Data_dlin_to_pred=np.array(Data_dlin_to_pred).reshape(-1,1)
    Data_est_to_pred=np.array(Data_est_to_pred).reshape(-1,1)
    Chisl_pred = model1.predict(Data_Chisl_to_pred)
    dlin_pred = model2.predict(Data_dlin_to_pred)
    est_pred = model3.predict(Data_est_to_pred)
    Data_pred_avg = []
    for i in range(len(vector)):
        Data_pred_avg.append((Chisl_pred[i]+dlin_pred[i]+est_pred[i])/3)
    return Data_pred_avg


# In[ ]:


def data_prep_pred(data_to_predict):
    data = host_to_domain(data_to_predict)
    est = estv(est_prep(data))
    vector = words_into_vector(data,est)
    return np.array(vector).reshape(-1,1)
