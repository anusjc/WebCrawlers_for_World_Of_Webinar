from requests import get

url = 'http://startupbuddy.co.in/events.php'

response = get(url)
#print(response.text[:500])

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

data_container = html_soup.findAll('div', class_ = 'col-sm-6 wow fadeInUp events')
#print(type(data_container))
print(len(data_container))

first_webinar = data_container[0]

title_webinar=first_webinar.find('h3',style='font-size:18px;').text

print(title_webinar)

image_first=first_webinar.find('img')
print(image_first.get('src'))

location=first_webinar.find('li',class_='locate').text
print(location)

date=first_webinar.find('li',class_='date').text
print(date)

link=first_webinar.find('a')
print(link['href'])


# title=[]
# link=[]
# image_link=[]
# dates=[]
# locations=[]


# for container in data_container:

#     #The Title
#     name=container.find('h3',style='font-size:18px;').text
#     title.append(name)

#     #The Link
#     links=container.find('a')
#     link.append(links['href'])

#     #The Image
#     image=container.find('img')
#     image_link.append(image.get('src'))

#     #The Date
#     date=container.find('li',class_='date').text
#     dates.append(date)

#     #The Location
#     location=container.find('li',class_='locate').text
#     locations.append(location)



# import pandas as pd

# test_df = pd.DataFrame({'Title': title,
#                        'Link': link,
#                        'Image': image_link,
#                        'Date': dates,
#                        'Location':locations})   
# test_df.to_csv("startupbuddy.csv")