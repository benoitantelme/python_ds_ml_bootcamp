#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Logistic Regression Project 
# 
# In this project we will be working with a fake advertising data set, indicating whether or not a particular internet
# user clicked on an Advertisement. We will try to create a model that will predict whether or not they will click on
# an ad based off the features of that user.
# 
# This data set contains the following features:
# 
# * 'Daily Time Spent on Site': consumer time on site in minutes
# * 'Age': cutomer age in years
# * 'Area Income': Avg. Income of geographical area of consumer
# * 'Daily Internet Usage': Avg. minutes a day consumer is on the internet
# * 'Ad Topic Line': Headline of the advertisement
# * 'City': City of consumer
# * 'Male': Whether or not consumer was male
# * 'Country': Country of consumer
# * 'Timestamp': Time at which consumer clicked on Ad or closed window
# * 'Clicked on Ad': 0 or 1 indicated clicking on Ad
# 
# ## Import Libraries
# 
# **Import a few libraries you think you'll need (Or just import them as you go along!)**

# In[38]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# ## Get the Data
# **Read in the advertising.csv file and set it to a data frame called ad_data.**

# In[39]:
ad_data = pd.read_csv('advertising.csv')

# **Check the head of ad_data**

# In[40]:
print(ad_data.head())

# ** Use info and describe() on ad_data**

# In[41]:
ad_data.info()
print(ad_data.describe())

# In[42]:


# ## Exploratory Data Analysis
# 
# Let's use seaborn to explore the data!
# 
# Try recreating the plots shown below!
# 
# ** Create a histogram of the Age**

# In[48]:
sns.set_style("whitegrid")
sns.distplot(ad_data['Age'], bins=30)
plt.show()

# **Create a jointplot showing Area Income versus Age.**

# In[64]:
sns.jointplot(x='Age', y='Area Income', data=ad_data, kind='scatter').annotate(stats.pearsonr)
plt.show()

# **Create a jointplot showing the kde distributions of Daily Time spent on site vs. Age.**

# In[66]:
sns.jointplot(x='Age', y='Daily Time Spent on Site', data=ad_data, kind='kde').annotate(stats.pearsonr)
plt.show()

# ** Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage'**

# In[72]:
sns.jointplot(x='Daily Internet Usage', y='Daily Time Spent on Site', data=ad_data, kind='scatter').annotate(
    stats.pearsonr)
plt.show()

# ** Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature.**

# In[84]:
sns.pairplot(ad_data, hue='Clicked on Ad')
plt.show()

# # Logistic Regression
# 
# Now it's time to do a train test split, and train our model!
# 
# You'll have the freedom here to choose columns that you want to train on!

# ** Split the data into training set and testing set using train_test_split**

# In[85]:
from sklearn.model_selection import train_test_split

ad_data.drop(['Ad Topic Line', 'City', 'Country', 'Timestamp'], axis=1, inplace=True)
X = ad_data.drop(['Clicked on Ad'], axis=1)
y = ad_data['Clicked on Ad']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)


# ** Train and fit a logistic regression model on the training set.**

# In[91]:
from sklearn.linear_model import LogisticRegression


# In[92]:
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

# ## Predictions and Evaluations
# ** Now predict values for the testing data.**

# In[94]:
predictions = logmodel.predict(X_test)

# ** Create a classification report for the model.**

# In[95]:
from sklearn.metrics import classification_report

# In[96]:
print(classification_report(y_test, predictions))

# ## Great Job!
