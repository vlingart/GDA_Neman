import pandas as pd
import random
from estv import estv
from turn_into_vector import words_into_vector
def est_prep(s):  #подготовка итоговой выборки доменов (удаление точек и дефисов))
    for i in range(len(s)):
        s[i]=s[i].replace('.','')
        s[i]=s[i].replace('-','')
        for j in range(10):
            s[i]=s[i].replace(str(j),'')
    return(s)
def host_to_domain(hosts):  #превращение домена в хост путем удаления доменов более высокого уровня, чем рассматриваемый
    for i in range(len(hosts)):
        hosts[i]=hosts[i][0:hosts[i].index('.')]
    return(hosts)
def domains_maker(Data):  #разбиение данной выборки на "хорошие" и "плохие" домены (сгенерированные и реальные)
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
def Data_Prep(data_name,purp):  #подготовка данных для дальнейшей кластеризации (перемешивание входных данных, создание векторов на основе слов, подсчет естественности каждого слова из учета реального языка)
    if(purp=='T'):
        Data=pd.read_csv(data_name)
        Good_domains,Bad_domains =domains_maker(Data)
        Y=[1]*len(Good_domains)+[0]*len(Bad_domains)
        Vyborka=host_to_domain(Good_domains)+host_to_domain(Bad_domains)
        Estestv_vyb=estv(est_prep(Vyborka))  #подсчет естественности (на основе частоты встречания биграмм в сети интернет)
        Vyborka=words_into_vector(Vyborka,Estestv_vyb)  #превращение слова в векторы (на основе количества определенных элементов в названии хоста+естественность+длина)
        Data_set=[]
        for i in range(len(Vyborka)):
            Data_set.append([Vyborka[i],Y[i]])
        random.shuffle(Data_set)  #перемешивание данных
        Data_train=Data_set[0:round(len(Data_set)*0.7)].copy()
        Data_valid=Data_set[round(len(Data_set)*0.7):].copy()
        X_train=[]
        Y_train=[]
        for i in Data_train:
            X_train.append(i[0])
            Y_train.append(i[1])
        X_valid=[]
        Y_valid=[]
        for i in Data_valid:
            X_valid.append(i[0])
            Y_valid.append(i[1])
    return([X_train,Y_train],[X_valid,Y_valid])
