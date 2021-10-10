#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries, website

# In[23]:


# Importing Libraries

import pandas as pd
from bs4 import BeautifulSoup
import requests 
import csv


# In[24]:


url= "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=7ec220e8-4f02-4150-9e0b-9e90cf692f4b&as-searchtext=laptop"


# In[25]:


# Importing website content

response=requests.get(url)
html_content= response.content
soup= BeautifulSoup(html_content, "html.parser")

print(soup.prettify)


# In[26]:


# Creating Lists

products= []  # List to save name of product
prices= []    # List to save price of product
ratings= []   # List to save rating of product


# In[27]:


# Taking an example of Data Scrapiing

product= soup.find("div", attrs={"class":"_4rR01T"})
print(product.text)


# In[28]:


# creating a loop to get data as text

for a in soup.findAll("a",href=True, attrs={"class":"_1fQZEK"}):
    name=a.find("div",attrs={"class":"_4rR01T"})
    price=a.find("div",attrs={"class":"_30jeq3 _1_WHN1"})
    rating=a.find("div",attrs={"class":"_3LWZlK"})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)


# In[29]:


# Creating Columns for Dataset

df=pd.DataFrame({"Products":products, "Prices":prices, "Ratings":ratings})
df.head()


# In[30]:


df.tail()


# In[31]:


# Saved Dataset on Users: Location

df.to_csv("Scraping.csv")


# In[ ]:




