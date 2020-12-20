#!/usr/bin/env python
# coding: utf-8

# In[14]:


import os
import matplotlib.pyplot as plt

jpgs=[]
for i in os.listdir("hangman"):
    jpgs.append(plt.imread("hangman/"+i))


# In[ ]:




