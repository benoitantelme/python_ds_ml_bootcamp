#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Seaborn Exercises
# 
# Time to practice your new seaborn skills! Try to recreate the plots below (don't worry about color schemes, just the
# plot itself.

# ## The Data
# 
# We will be working with a famous titanic data set for these exercises. Later on in the Machine Learning section of
# the course, we will revisit this data, and use it to predict survival rates of passengers. For now, we'll just focus
# on the visualization of the data with seaborn:

# In[19]:


import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# get_ipython().run_line_magic('matplotlib', 'inline')


# In[27]:


sns.set_style('whitegrid')

# In[28]:


titanic = sns.load_dataset('titanic')

# In[40]:


titanic.head()

# # Exercises
# 
# ** Recreate the plots below using the titanic dataframe. There are very few hints since most of the plots can be
# done with just one or two lines of code and a hint would basically give away the solution. Keep careful attention to
# the x and y labels for hints.**
# 
# ** *Note! In order to not lose the plot image, make sure you don't code in the cell that is directly above the plot,
# there is an extra cell above that one which won't overwrite that plot!* **

# In[42]:
sns.set_style("whitegrid", {'grid.linestyle': '-'})
sns.jointplot(x='fare', y='age', data=titanic, kind='scatter').annotate(stats.pearsonr)
plt.show()

# In[43]:
sns.distplot(titanic['fare'], kde=False, color='red')
plt.show()
# In[44]:

# print(titanic.columns)

sns.boxplot(x='class', y='age', data=titanic)
plt.show()

# In[ ]:


# In[45]:
sns.swarmplot(x='class', y='age', data=titanic)
plt.show()
# In[ ]:


# In[46]:
sns.countplot(x='sex', data=titanic)
plt.show()
# In[ ]:


# In[47]:
sns.heatmap(titanic.corr(), cmap='coolwarm')
plt.title("correlation")
plt.show()
# In[ ]:


# In[48]:
g = sns.FacetGrid(titanic, col="sex")
g = g.map(plt.hist, "age")
plt.show()
# In[ ]:


# In[49]:




# # Great Job!
# 
# ### That is it for now! We'll see a lot more of seaborn practice problems in the machine learning section!
