#!/usr/bin/env python
# coding: utf-8

# In[213]:


import pandas as pd
import random
from estv import estv
from turn_into_vector import words_into_vector
def est_prep(s):
    for i in range(len(s)):
        s[i]=s[i].replace('.','')
        s[i]=s[i].replace('-','')
        for j in range(10):
            s[i]=s[i].replace(str(j),'')
    return(s)
def host_to_domain(hosts):
    for i in hosts:
        i=i[0:i.index('.')]
    return(hosts)
def domains_maker(Data):
    s_c=[]
    for i in range(len(Data.subclass)):
        if(Data.subclass[i] not in s_c):
            s_c.append(Data.subclass[i])
    s_c.remove('legit')
    vybr=[]
    Good_domains=[]
    Bad_domains=[]
    for i in range(len(Data.host)):
        if(Data['class'][i]== 'legit') or(Data.subclass[i]== 'legit'):
            Good_domains.append(Data.host[i])
        if(Data['class'][i]== 'dga') or(Data.subclass[i] in s_c ):
            Bad_domains.append(Data.host[i])
    for i in Bad_domains:
        if  ('\n' in i):
            Bad_domains.remove(i) 
    return(Good_domains,Bad_domains)
def Data_Prep(data_name,purp):
    if(purp=='T'):
        Data=pd.read_csv(data_name)
        Good_domains,Bad_domains =domains_maker(Data)
        Y=[1]*len(Good_domains)+[0]*len(Bad_domains)
        Vyborka=host_to_domain(Good_domains)+host_to_domain(Bad_domains)
        Estestv_vyb=estv(est_prep(Vyborka))
        Vyborka=words_into_vector(Vyborka,Estestv_vyb)
        Data_set=[]
        for i in range(len(Vyborka)):
            Data_set.append([Vyborka[i],Y[i]])
        random.shuffle(Data_set)
        Data_train=Data_set[0:round(len(Data_set)*0.7)].copy()
        Data_valid=Data_set[round(len(Data_set)*0.7):].copy()
        X_train=[]
        Y_train=[]
        for i in Data_train:
            X_train.append(i[0])
            Y_train.append(i[1])
    return([X_train,Y_train],Data_valid,)
Data_Prep('dataset_isp.csv',purp='T')


# In[214]:





# In[ ]:




