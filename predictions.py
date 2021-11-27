#!/usr/bin/env python
# coding: utf-8


# In[ ]:


def get_predictions(vectors,model1,model2,model3):
    Data_Chisl_to_pred=[]
    Data_dlin_to_pred=[]
    Data_est_to_pred=[]
    for i in range(len(vector)):
        Data_Chisl_to_pred.append(vector[i][0:36])
        Data_dlin_to_pred.append(vector[i][37])
        Data_est_to_pred.append(vector[i][36])
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
    return vector

