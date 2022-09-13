#!/usr/bin/env python
# coding: utf-8

# In[259]:


import requests


# In[266]:


def yesno(url):
    try:
        r = requests.get(url, timeout=4)
        
        newstr = r.url
        print(newstr)

        newspl = newstr.split('.')
        print(newspl)

        if('myshopify' in newspl):
            print("YES")

        else:
            print("NO")
    
    except:
        print("NO")


# In[267]:


def shopify(url):   
    
    ustr = url
    
    spl = ustr.split('/')
    print(spl)

    if (spl[0] == 'http:' or spl[0] == 'https:' ):
        yesno(url)
        

    else:
        url = "https://"+ url
        yesno(url)


# In[268]:


ip_url = input("Enter URL : ")


# In[269]:


shopify(ip_url + "/admin")


# In[ ]:




