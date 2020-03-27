#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:

import numpy as np

# #### Create an array of 10 zeros

# In[2]:


print(np.zeros(10))

# #### Create an array of 10 ones

# In[3]:


print(np.ones(10))

# #### Create an array of 10 fives

# In[4]:

print(np.array([5] * 10))
print(np.full(10, 5))

# #### Create an array of the integers from 10 to 50

# In[5]:

print(np.arange(10, 51))

# #### Create an array of all the even integers from 10 to 50

# In[6]:

print(np.arange(10, 51, 2))

# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[7]:

print(np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))

# #### Create a 3x3 identity matrix

# In[8]:

print(np.eye(3))

# #### Use NumPy to generate a random number between 0 and 1

# In[15]:

print(np.random.randint(0, 2))

# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[33]:

print(np.random.randn(25))

# #### Create the following matrix:

# In[35]:

print(np.arange(0, 1.01, 0.01))

# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[36]:


print(np.linspace(0, 1, 20))

# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[38]:


mat = np.arange(1, 26).reshape(5, 5)
print(mat[2:, 1:])
# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[40]:
print(mat[3, 4])

# In[29]:
print(mat[:3, 1])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[41]:
print(mat[4:])

# In[30]:
print(mat[3:])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[42]:


# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[46]:


# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[49]:


# ### Now do the following

# #### Get the sum of all the values in mat

# In[50]:
print(np.sum(mat))

# #### Get the standard deviation of the values in mat

# In[51]:
print(np.std(mat))

# #### Get the sum of all the columns in mat

# In[53]:
print(mat.sum(axis=0))
mat.sum(axis=0)

# # Great Job!
