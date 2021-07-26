from requests import get

url ='https://craftjam.co/virtual/attend'

response = get(url)
#print(response.text[:500])

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

data_container = html_soup.findAll('div', class_='summary-content sqs-gallery-meta-container')
data_image=html_soup.findAll('div',class_='summary-thumbnail img-wrapper')
print(len(data_image))
print(len(data_container))
#till above code we will get the amount of Data Containers in that page
first_webinar = data_container[0]
first_image=data_image[0]

 #From this we got the Title for our webinar    
title_webinar=first_webinar.find('a',class_='summary-title-link').text
print(title_webinar)         
# Image of Webinar
image_webinar=first_image.find('img')
print(image_webinar.get('data-src'))
#Date of Webinar
date_webinar=first_webinar.find('div',class_='summary-metadata summary-metadata--primary').text
print(date_webinar)
# Time of Webinar
time_webinar=first_webinar.find('span',class_='event-time-12hr').text
print(time_webinar)
#From this we got the link of Webinar to register
link_first=first_webinar.find('a')
print('https://craftjam.co'+link_first.get('href')) 
#Agenda
about=first_webinar.find('p').text
print(about)

title=[]
image=[]
date=[]
time=[]
link=[]
about=[]

for container in data_container:

    #Title
    name=container.find('a',class_='summary-title-link').text
    title.append(name)
    #link
    lnnk=container.find('a')
    lnk='https://craftjam.co' + lnnk.get('href')
    link.append(lnk)
    #Time
    tm=container.find('span',class_='event-time-12hr').text
    time.append(tm)
    #Date
    dt=container.find('div',class_='summary-metadata summary-metadata--primary').text
    date.append(dt)
    #About/Agenda
    aj=container.find('p').text
    about.append(aj)

#This Loop is for image
for i in  data_image:
    img=i.find('img')
    image.append(img.get('data-src'))   

import pandas as pd

test_df = pd.DataFrame({'Topic of the webinar': title,
                       'Date': date,
                       'Time': time,
                       'Start Time':' ',
                       'End  Time':' ',
                       'Duration':' ' ,
                       'Image': image,
                       'Link of the webinar': link,
                       'Organising Body':'Craft Jam',
                       'Key Take aways / Agenda':about,
                       'Platform':'Zoom',
                       'Price (Free/Paid)':'Paid'
                       })
# print(test_df)

test_df.to_csv("craftjam0608.csv")  


