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