#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Assignment: Segmenting and Clustering Neighborhoods in Toronto


# In[3]:


import sys
get_ipython().system('{sys.executable} --version')


# In[2]:


get_ipython().system('pip --version')


# In[4]:


## installing beautifulsoup


# In[5]:


get_ipython().system('pip install beautifulsoup4')


# In[11]:


# importing packages bs4,beautifulSoup,requests and pandas


# In[6]:


import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[ ]:


# web scraing the table data  from the website link using BeautifulSoup


# In[7]:


source=requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup= BeautifulSoup(source,'html5lib')
table=soup.find('table',class_='wikitable sortable')
table_rows=table.find_all('tr')
# assigning columns 
d_key=['name','borough','neighborhood']
da=[]
for tr in table_rows :
    t_row = {}
    for td, th in zip(tr.find_all("td"), d_key): 
            t_row[th] = td.text.replace('\n', '').strip()
    da.append(t_row)
        


# In[8]:


len(da)


# In[9]:


da.pop(0)


# In[ ]:


# total no.of rows from data is 287


# In[10]:


len(da)


# In[ ]:


# ignoring the rows  where borough='not assigned'


# In[12]:


my_list=[i for i in da if not(i['borough']=='Not assigned')]
print(my_list)


# In[ ]:


# number of rows after ignoring the borough='Not assigned' is 210


# In[13]:


len(my_list)


# In[ ]:


#selecting rows where neighborhood='not asssigned 'and changing the value


# In[14]:


my_list1=[i for i in my_list if(i['neighborhood']=='Not assigned')]

print(my_list1)


# In[15]:


for list1 in my_list1:
    dic=list1
    for key, value in dic.items():
     if( value == "Not assigned"):
        dic.pop(key,'Not assigned')
        dic[key] =dic['borough']
print (dic)
    


# In[16]:


# appending the changed rows to the list of rows and converting to a dataframe


# In[17]:


my_list.append(dic)


# In[18]:


import pandas as pd
df=pd.DataFrame(my_list)
#df.shape
df.head()


# In[20]:


df.shape


# In[ ]:


# checking for duplicate rows in dataframe


# In[21]:


print (any(df.neighborhood =="Not assigned"))
       #true if it contains


# In[ ]:


#sorting the dataframe based on name and borough


# In[22]:


df2=(df.sort_values(by=['name','borough'],inplace=False)).reset_index(drop=True)
df2


# In[23]:


# grouping the dataframe based on name and borough and printing the groups


# In[24]:


grouped = df2.groupby(['name', 'borough'], as_index=False)
print(grouped.count())


# In[ ]:


# converting the groups neighborhood columns with more than one neighborhood and appending it to list


# In[26]:


newls=[]
neigh=[]
i=0
newstr=""
while(i<103): 

    for key, group in grouped:
         #print("key:",key,"group:",list(group['neighborhood']) )
         neigh=list(group['neighborhood'])
         #print(neigh)
         newstr=','.join(str(x) for x in (list(group['neighborhood'])))
         #print(newstr)
         L1=list(key)
         L1.append(newstr)
         T1=tuple(L1)
         #print(T1)
         newls.append(T1)
    if (len(newls)==103):
           break;
    i=i+1
print(newls)
        


# In[ ]:


#converting the list back to Dataframe


# In[27]:


newdf=pd.DataFrame(newls,columns=d_key)


# In[28]:


newdf.head(10)


# In[ ]:


#shape of the final dataframe 


# In[29]:


newdf.shape

