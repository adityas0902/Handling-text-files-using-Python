#!/usr/bin/env python
# coding: utf-8

# # Importing library 

# In[29]:


import re
import pandas as pd
from collections import defaultdict


# # Read the text file

# In[19]:


with open('conv.txt', 'r') as file:
    content = file.read()


# ## Split the content into lines

# In[45]:


match = content.split('\n')
print(lines)


# #  Extract unique dialogue speakers and their dialogues

# In[33]:



dialogues = defaultdict(str)
for line in lines:
    match = re.match(r'^(.+?):\s*(.+)$', line)
    if match:
        speaker, dialogue = match.groups()
        dialogues[speaker] += dialogue + ' '


# In[44]:


Unique_Name = set(dialogues.keys())


# #  Process each speaker's dialogues

# In[22]:


for speaker, dialogue in dialogues.items():
    # Extract unique words
    words = set(re.findall(r'\b\w+\b', dialogue.lower()))
    
    # Create a new text file and store unique words
    with open(f'{speaker}.txt', 'w') as file:
        for word in sorted(words):
            file.write(f'{word}\n')

