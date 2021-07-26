title=[]
# link=[]
# image_link=[]
# description=[]

# # Extract data from individual data container

# for container in data_container:

#     #The Title
#     name=container.h3.text
#     title.append(name)   


#     #The Link
#     link_go=container.find('a',class_='ps-button ps-button--full ps-button--m ps-button--link event-cta-rsvp')   
#     link.append(link_go['href'])


#     #The Image Link
#     img_link=container.find('img')
#     image_link.append(img_link.get('data-src'))

#     #The Description
#     description_first=[]
#     for date in container.find_all('span',class_='li-text'):
#         description_first.append(date.text)
#     description.append(description_first)
     
      
# import pandas as pd

# test_df = pd.DataFrame({'Title': title,
#                        'Link': link,
#                        'Image': image_link,
#                        'Description': description})
# #print(test_df)

# test_df.to_csv("data.csv")