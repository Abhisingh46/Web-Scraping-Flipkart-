#!/usr/bin/env python
# coding: utf-8

# In[1]:


from autoscraper import AutoScraper


# In[2]:


flip_url="https://www.flipkart.com/search?q=iphone+below+50%2C000&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=2&as-type=HISTORY"
wanted_list=["₹49,900","APPLE iPhone 11 (Green, 64 GB)"]


# In[4]:


scraper=AutoScraper()
result=scraper.build(flip_url,wanted_list)
print(result)


# In[6]:


scraper.get_result_similar(flip_url,grouped=True)


# In[10]:


scraper.set_rule_aliases({'rule_3dgw':'Title','rule_9pk7':'Price'})
scraper.keep_rules(['rule_3dgw','rule_9pk7'])
scraper.save('flipkart.search')


# In[19]:


final_results=scraper.get_result_similar("https://www.flipkart.com/search?q=mobile+under+10000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_7_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_3_7_na_na_ps&as-pos=3&as-type=RECENT&suggestionId=mobile+under+10000&requestId=ba9fd23d-2752-4c12-b1a0-a5e9d641bdc1&as-backfill=on",group_by_alias=True)
final_results["Title"]


# In[ ]:




