#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os


# In[32]:


data = pd.read_csv("apple_productss.csv")
print(data.head())


# In[33]:


print(data.describe())


# In[34]:


highest_rated = data.sort_values(by=["Star Rating"], 
                                 ascending=False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])


# In[35]:


iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label, 
                y = counts, 
            title="Number of Ratings of Highest Rated iPhones")
figure.show()


# In[36]:


iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label, 
                y = counts, 
            title="Number of Reviews of Highest Rated iPhones")
figure.show()


# In[37]:


figure = px.scatter(data_frame = data, x="Number Of Ratings",
                    y="Sale Price", size="Discount Percentage", 
                    trendline="ols", 
                    title="Relationship between Sale Price and Number of Ratings of iPhones")
figure.show()


# In[38]:


figure = px.scatter(data_frame = data, x="Number Of Ratings",
                    y="Discount Percentage", size="Sale Price", 
                    trendline="ols", 
                    title="Relationship between Discount Percentage and Number of Ratings of iPhones")
figure.show()

