#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


d=pd.read_csv(r"C:\Users\vsvij\Documents\Pandas project File\Weather File.csv")


# In[7]:


d


# In[8]:


d.head()


# In[9]:


d.shape


# In[10]:


d.columns


# In[12]:


d.dtypes


# In[15]:


d['Weather'].unique()


# In[17]:


d.nunique()


# In[18]:


d.count()


# In[19]:


d['Weather'].value_counts()


# In[20]:


d.info()


# In[21]:


d.head(2)            #Q1


# In[23]:


d.nunique()


# In[24]:


d['Wind Speed_km/h'].nunique()


# In[26]:


d['Wind Speed_km/h'].unique()   #A1


# In[27]:


d.head(2)                #Q2


# In[29]:


d.Weather.value_counts()             #value_counts


# In[30]:


d.head(2)   #Flitering


# In[32]:


d.Weather == 'Clear'


# In[33]:


d[d.Weather == 'Clear']


# In[34]:


d.head(2)          #Groupby


# In[35]:


d.groupby('Weather').get_group('Clear')   #A2


# In[36]:


d.head(2)          #Q3


# In[38]:


d['Wind Speed_km/h'] == 4


# In[39]:


d[d['Wind Speed_km/h'] == 4]  #A3


# In[40]:


d.isnull()          #Q4


# In[41]:


d.isnull().sum()


# In[42]:


d.notnull().sum()      #A4


# In[43]:


d.head(2)             #Q5


# In[44]:


d.rename(columns = {'Weather' : 'Weather Condition'})


# In[45]:


d.head()


# In[46]:


d.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)


# In[47]:


d.head()  #A5


# In[48]:


d.head(2)         #Q6


# In[49]:


d.Visibility_km.mean()  #A6


# In[50]:


d.Press_kPa.std()        #Q7 & A7


# In[51]:


d['Rel Hum_%'].var()     #Q8 & A8


# In[52]:


#value_counts()    #Q9
d.head(2)


# In[53]:


d['Weather Condition'].value_counts()


# In[56]:


#flitering
d[d['Weather Condition'] == 'Snow']


# In[60]:


#str.contains
d[d['Weather Condition'].str.contains('Snow')]


# In[62]:


d[d['Weather Condition'].str.contains('Snow')].head(50)


# In[63]:


d[d['Weather Condition'].str.contains('Snow')].tail(50)  #Q9


# In[64]:


d.head(2)         #Q10


# In[65]:


d[(d['Wind Speed_km/h'] > 24) & (d['Visibility_km'] == 25)]  #A10


# In[66]:


d.head(2)       #Q11


# In[68]:


d.groupby('Weather Condition').mean()  #A11


# In[69]:


d.head(2)  #Q12


# In[70]:


d.groupby('Weather Condition').min()


# In[71]:


d.groupby('Weather Condition').max()  #A12


# In[72]:


d[d['Weather Condition'] == 'Fog'] #Q13 & #A13


# In[75]:


d[(d['Weather Condition'] == 'Clear') | (d['Visibility_km'] > 40)]             #Q14


# In[76]:


d[(d['Weather Condition'] == 'Clear') | (d['Visibility_km'] > 40)].head(50)             #Q14


# In[77]:


d.head(2)   #Q15


# In[81]:


d[(d['Weather Condition'] == 'Clear') & (d['Rel Hum_%'] > 50) | (d['Visibility_km'] > 40)]


# In[ ]:




