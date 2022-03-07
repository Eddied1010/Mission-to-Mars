#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[ ]:


#
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[71]:


slide_elem.find('div', class_='content_title')


# In[72]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[73]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Feauture Images
# 

# In[74]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[18]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[22]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[23]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[24]:


df.to_html


# In[ ]:


browser.quit()


# Start of Class Challenge

# ### D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[ ]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')


# In[78]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
hemisphere_image_urls = img_soup.find('img', class_='wide-image').get('src')
hemisphere_image_urls
#for i in img_soup.find_all('img', class_='wide-image'):
#    hemisphere_image_urls.append('src')
#hemisphere_image_urls = img_soup.find_all('img', class_='thumb')
#hemisphere_image_urls

# Use the base URL to create an absolute URL
img_url = f'https://marshemispheres.com/{hemisphere_image_urls}'
img_url

slide_elem.find_all('div', class_='title')

# Use the parent element to find the first `a` tag and save it as `news_title`
mars_title = slide_elem.find_all('div', class_='title').get_text()
mars_title

# 3. Write code to retrieve the image urls and titles for each hemisphere.
For x in hemisphere_image_urls:
    hemisphere_images_urls.append()
for z in mars_title:
    mars_title.append()
    


# In[ ]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls
mars_title


# In[75]:


# 5. Quit the browser
browser.quit()


# In[ ]:


# 6 write code to retrieve the full-resolution image URL and title for each hemisphere image. The full-resolution image will have the .jpg extension.
full_image_urls = img_soup.find('a', target_='blank').get('href')
full_image_urls
hemi_title = slide_elem.find_all('h2', class_='title').get_text()
hemi_title


# In[84]:


#7 Loop through the full-resolution image URL, click the link, find the Sample image anchor tag, and get the href.
sample_image =[]

for i in sample_image:
    sample_image = img_soup.find('a', target_='blank', 'sample').get('href')[0]
    sample_image.append()
        


# In[ ]:




