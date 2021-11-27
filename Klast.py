#!/usr/bin/env python
# coding: utf-8

# In[26]:


from Data_prep import Data_Prep
from sklearn.neural_network import MLPClassifier
import numpy as np
from turn_into_vector import words_into_vector


# In[2]:


Data_train,Data_valid=Data_Prep('dataset_clear.csv',purp='T')


# In[19]:


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


# In[18]:


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


# In[12]:


Est_model=MLPClassifier((20,20,20,20,20,20,20), random_state=1,activation='logistic',max_iter=300)
Est_model.fit(Data_est_train,Data_y)
Est_model.score(Data_est_valid,Data_y_valid)


# In[20]:


Ch_model=MLPClassifier((20,20,20,20,20,20,20), random_state=1,activation='logistic',max_iter=300)
Ch_model.fit(Data_Chisl_train,Data_y)
Ch_model.score(Data_Chisl_valid,Data_y_valid)


# In[14]:


Dl_model=MLPClassifier((20,20,20,20,20,20,20), random_state=1,activation='logistic',max_iter=300)
Dl_model.fit(Data_dlin_train,Data_y)
Dl_model.score(Data_dlin_valid,Data_y_valid)


# In[ ]:





# In[73]:


Ch_model.predict(a)


# In[38]:


a=np.array([1,2,34])


# In[41]:


a.reshape(-1,1)


# In[44]:


Data_est_train


# In[ ]:




