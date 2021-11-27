#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import numpy as np

def get_data(Data):
    Data_Chisl=[]
    Data_dlin=[]
    Data_est=[]
    for i in range(len(Data[0])):
        Data_Chisl.append(Data[0][i][0:36])
        Data_dlin.append(Data[0][i][37])
        Data_est.append(Data[0][i][36])
    Data_y=Data[1]
    Data_Chisl=np.array(Data_Chisl)
    Data_dlin=np.array(Data_dlin).reshape(-1,1)
    Data_est=np.array(Data_est).reshape(-1,1)
    return(Data_Chisl,Data_dlin,Data_est)

