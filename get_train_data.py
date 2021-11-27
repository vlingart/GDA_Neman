#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_train_data(Data_train):
    Data_Chisl_train=[]
    Data_dlin_train=[]
    Data_est_train=[]
    for i in range(len(Data_train[0])):
        Data_Chisl_train.append(Data_train[0][i][0:36])
        Data_dlin_train.append(Data_train[0][i][37])
        Data_est_train.append(Data_train[0][i][36])
    Data_y=Data_train[1]
    Data_Chisl_train=np.array(Data_Chisl_train)
    Data_dlin_train=np.array(Data_dlin_train).reshape(-1,1)
    Data_est_train=np.array(Data_est_train).reshape(-1,1)
    return(Data_Chisl_train,Data_dlin_train,Data_est_train)

