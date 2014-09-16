
# coding: utf-8

# Change the stroop script to use functions

# In[1]:

import os
os.getcwd()


# In[4]:

mon_fichier = open('nouveau_fichier.txt','w')


# In[5]:

mon_fichier.close()


# if you modify the file and open it again, it is erased!!!!!

# In[8]:

mon_fichier = open('nouveau_fichier.txt','w')
mon_fichier.write('bla bla bla')
mon_fichier.close()


# In[7]:




# In[ ]:

mon_fichier = open('nouveau_fichier.txt','w')
mon_fichier.write('bla\nbla\bla')
mon_fichier.close()

