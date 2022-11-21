# pip install requests
# pip install bs4
# pip install html5lib


from xml.dom.minidom import Element
import requests
from bs4 import BeautifulSoup
# url = "https://www.codewithharry.com"
url = "https://www.flipkart.com/search?q=iphone11"

# Step 1: Get the HTML
r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify) 
 
# Step 3: HTML Tree Traversal
# Commonly ussed types of objects.
                   
# print(type(title))          # 1. Tag
# print(type(title.string))   # 2. Navigable String
# print(type(soup))           # 3. BeautifulSoup 

# 4. Comment

# Get the title of HTML page
title = soup.title

# Get all the paragraph from the page 
paras = soup.find_all('p')
# print(paras)


# Get 1st element in the HTML page 
# print(soup.find('p'))

# Get class of any element in the HTML Page
# print(soup.find('p')['class'])

# find all the elements with class mt-2 
# print(soup.find_all("p",class_= "mt-2"))

# get the text from the tag/soup
# print(soup.find('p').get_text()) 
# print(soup.get_text())

# Get all the anchir tags from the page 
anchors = soup.find_all('a')
# print(anchors)
all_links = set()

# Get all the links on the page:
for link in anchors:
    if(link != '#'):
        # linktext = "https://codewithharry.com" + link.get('href')
        linktext = url + link.get('href')
        all_links.add(linktext)
        print(linktext)