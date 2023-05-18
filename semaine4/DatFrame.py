#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df3 = pd.DataFrame([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150], 
                  [160, 170, 180, 190, 200],
                  [210, 220, 230, 240, 250]], index = ['a', 'b', 'c', 'd', 'e'], columns = list('vwxyz'))

 

df3


# In[4]:


df3.loc['a', ['x' , 'y']]


# In[5]:


df3.loc['a', 'x']


# In[6]:


df3.loc[['a', 'c'], 'z']


# In[9]:


df3.loc[df3.x > 200]


# In[16]:


mask = df3.x > 200
df3.loc[mask]


# In[18]:


df3.loc[mask , ['x', 'y']]


# In[23]:


df3.loc[df3.x > 200 , df3.loc['c'] > 135]


# In[29]:


df3.loc[df3.x > 180]


# In[30]:


df3['y']['b'] = 123 #replace value 


# In[31]:


df3


# In[33]:


df4 = pd.DataFrame([{'product_id':23, 'name':'computer', 'wholesale_price': 500,
        'retail_price':1000, 'sales':100},
        {'product_id':96, 'name':'Python Cours', 'wholesale_price': 35,
        'retail_price':75, 'sales':1000},
        {'product_id':97, 'name':'Pandas Cours', 'wholesale_price': 35,
        'retail_price':75, 'sales':500},
        {'product_id':15, 'name':'banana', 'wholesale_price': 0.5,
        'retail_price':1, 'sales':200},
        {'product_id':87, 'name':'sandwich', 'wholesale_price': 3,
        'retail_price':5, 'sales':300},
        ])
df4


# In[38]:


df4['current_net'] = [50000.0, 40000.0, 20000.0, 100.0, 600.00]

df4['after_15'] = df4['current_net'] * 0.85

df4['after_20'] = df4['current_net'] * 0.80


# In[39]:


df4['after_25'] = df4['current_net'] * 0.75


# In[40]:


df4


# In[64]:


df4.loc[df4['retail_price'] > 80 , 'new_price']= df4['retail_price'] + df4['retail_price'] * 0.75
df4.loc[(df4['retail_price'] > 30) & (df4['retail_price'] <= 80), 'new_price']= df4['retail_price'] + df4['retail_price'] * 0.9
df4.loc[df4['retail_price'] < 30 , 'new_price']= df4['retail_price'] + df4['retail_price'] * 0.05


# In[65]:


df4


# In[67]:


#create 2nd dataframe and merge two
import pandas as pd
df5 = pd.DataFrame([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150], 
                  [160, 170, 180, 190, 200],
                  [210, 220, 230, 240, 250]], index = ['a', 'b', 'c', 'd', 'e'], columns = list('vwxyz'))

 

df5


# In[71]:


df6 = pd.DataFrame([[10, 20, 30, 40, 50]], index = ['a'], columns = list('vwxyz'))
df6


# In[72]:


#merge two dataframe

merged = df5.append(df6)
merged


# In[75]:


merged = df5.append(df6)
merged


# In[79]:


merged_2 = pd.concat([df5, df6])
merged_2


# In[84]:


#pd.concat([df5, df6], axis=1) concatenates the DataFrames df5 and df6 horizontally along the columns.
#The axis=1 parameter specifies that the concatenation should be performed along the columns.

merged_2 = pd.concat([df5, df6] , axis = 1)
merged_2


# In[99]:


df9= pd.DataFrame([{'product_id':23, 'name':'computer', 'wholesale_price': 500,
        'retail_price':1000, 'sales':100},
        {'product_id':96, 'name':'Python Cours', 'wholesale_price': 35,
        'retail_price':75, 'sales':1000},
        {'product_id':97, 'name':'Pandas Cours', 'wholesale_price': 35,
        'retail_price':75, 'sales':500},
        {'product_id':15, 'name':'banana', 'wholesale_price': 0.5,
        'retail_price':1, 'sales':200},
        {'product_id':87, 'name':'sandwich', 'wholesale_price': 3,
        'retail_price':5, 'sales':300},
        ])
df9


# In[109]:


df7= pd.DataFrame([{'product_id': 24 , 'name': 'phone', 'wholesale_price': 200, 'retail_price': '', 'sales': ''},
                   {'product_id': 32 , 'name': 'mobile', 'wholesale_price': 150, 'retail_price': '', 'sales': ''}, ],
                      index  = range(5, 7))
df7


# In[110]:


new_df = pd.concat([df9, df7])
new_df


# In[115]:


#fill empty values
new_df.loc[[5, 6] , 'sales'] = [520, 310]
new_df.loc[[5, 6] , 'retail_price'] = [100, 200]
new_df


# In[116]:


new_df.head()


# In[122]:


new_df[['product_id', 'name']].head()


# In[131]:


#quantile
import pandas as pd
s = pd.Series([350, 450, 550, 650, 750, 850, 950])


# In[136]:


q1 = s.quantile(0.75)
q2 = s.quantile(0.25)


# In[138]:


q = q1 - q2
q


# In[ ]:




