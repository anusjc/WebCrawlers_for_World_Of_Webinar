from requests import get

url = 'https://www.productschool.com/product-management-events/'

response = get(url)
#print(response.text[:500])

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

data_container = html_soup.find_all('div', class_ = 'ps-card-event__wrapper ps-card-event__with-thumb vc_column_container vc_col-xs-12 vc_col-sm-6 col-md-4 wow fadeInUp')
#print(type(data_container))
print(len(data_container))
#till above code we will get the amount of Data Containers in that page
# first_webinar = data_container[0]

# title_first=[]        
# title_webinar=first_webinar.h3.text  
# title_first.append(title_webinar)          #From this we got the Title for our webinar 
# #---------------------------------------------------------------------------------------------

# links_first=[]
# link_first=first_webinar.find('a',class_='ps-button ps-button--full ps-button--m ps-button--link event-cta-rsvp')
# links_first.append(link_first) #From this we got the link of Webinar to register
       
# #------------------------------------------------------------------------------------------------
# image_link_first=[]
# image_first=first_webinar.find('img')
# image_link_first.append(image_first)   #From this we will get the link of image

      
# #-------------------------------------------------------------------------------------------------
# description_first=[]
# for date in first_webinar.find_all('span',class_='li-text'):
#     description_first.append(date.text)       #From this we will get the Description of the webinar

#---------------------------------------------------------------------------------------------------
# emage=first_webinar.find('ul',class_='ps-card-event__list')
# print(emage.text)
# print all the Details:
# print(title_first)
# print(links_first)
# print(image_link_first)
# print(description_first)
#----------------------------------------------------------------------------------------------------
#We are making containers for our data to enter
title=[]
link=[]
image_link=[]
# description=[]
Author=[]
Date=[]
time=[]
# medium=[]

# Extract data from individual data container

for container in data_container:

    #The Title
    name=container.h3.text
    title.append(name)   


    #The Link
    link_go=container.find('a',class_='ps-button ps-button--full ps-button--m ps-button--link event-cta-rsvp')   
    link.append(link_go['href'])


    #The Image Link
    img_link=container.find('img')
    image_link.append(img_link.get('data-src'))

    #The Description
    description_first=container.find_all('span',class_='li-text')
    # print(len(description_first))
    # Author.append(description_first[0].text)
    Date.append(description_first[1].text)
    time.append(description_first[2].text)
    # medium.append(description_first[3])

    
     
      
import pandas as pd

test_df = pd.DataFrame({'Topic of the webinar': title,
                       'Date':Date,
                       'time':time,
                       'Start Time':' ',
                       'End  Time':' ',
                       'Duration':' ' ,
                       'Organising Body':'Product School',
                       'Link of the webinar': link,
                       'Image': image_link,
                       'Key Take aways / Agenda':' ',
                       'Platform':'Website'
                       
                       })
                    #    'medium':medium
#print(test_df)

test_df.to_csv("product0910.csv")
  








