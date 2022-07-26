#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
df1=pd.read_csv("C:\\Users\\Ramatu\\.jupyter\\dataset\\FOA.csv" , encoding='latin-1')
df1.head()


# In[11]:


df1.describe()


# In[12]:


df1.isnull().sum()


# In[13]:


df1 = df1.fillna(df1.mean())
df1.head()


# In[14]:


df1.isnull().sum()


# In[ ]:




