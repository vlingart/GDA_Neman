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


# In[ ]:


def get_valid_data(Data_valid):
    Data_Chisl_valid=[]
    Data_dlin_valid=[]
    Data_est_valid=[]
    for i in range(len(Data_valid[0])):
        Data_Chisl_valid.append(Data_valid[0][i][0:36])
        Data_dlin_valid.append(Data_valid[0][i][37])
        Data_est_valid.append(Data_valid[0][i][36])
    Data_y_valid=Data_valid[1]
    Data_Chisl_valid=np.array(Data_Chisl_valid)
    Data_dlin_valid=np.array(Data_dlin_valid).reshape(-1,1)
    Data_est_valid=np.array(Data_est_valid).reshape(-1,1)
    return(Data_Chisl_valid,Data_dlin_valid,Data_est_valid)


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

