
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


car=pd.read_csv(r'C:\Users\HP\OneDrive\Documents\car.csv')


# In[4]:


car.head(10)


# In[9]:


car.columns.unique()


# In[10]:


car.shape


# In[15]:


#find if there is any null value in any columns
car.isnull().sum()


# In[20]:


#to fill the null values with the mean value
car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)
car.isnull().sum()


# In[29]:


car['Make'].value_counts() #this is to find the no. of frequency of any item there in "Make" column


# In[31]:


#to filter out the records having asia and europe in it using this syntax in origin column
car[car['Origin'].isin(['Asia','Europe'])] 


# In[32]:


car[~(car['Weight']>4000)]


# In[33]:


car[(car['Weight']>4000)]


# In[35]:


car.shape


# In[36]:


car[~(car['Weight']>4000)] # this syntax is to remove the rows with the condition


# In[37]:


# increase all the values of column 'MPG_CITY' by 3
car.head(2)


# In[43]:


# We use this type of data 
car['MPG_City']=car['MPG_City'].apply(lambda x:x+3)


# In[44]:


car.head(100)


# In[ ]:




