#!/usr/bin/env python
# coding: utf-8

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

