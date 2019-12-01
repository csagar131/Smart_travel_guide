#!/usr/bin/env python
# coding: utf-8

# In[35]:


import googlemaps
import folium
import time


# In[29]:


#define our client
api_key="AIzaSyAWmyrQyw7hRpYIHGTEDJlj09fTLSG_MDA"
gmaps = googlemaps.Client(api_key)


# In[36]:


your_city = input("Where do you live :- ").replace(' ','+')
current_location = gmaps.geocode(your_city)
time.sleep(3)


# In[31]:


#this will print latitude and longitude of current location
user_city = list(current_location[0]['geometry']['location'].values())
#print(user_city)
user_city_string=[str(i) for i in user_city]
city_string=','
city_string=city_string.join(user_city_string)
#print(city_string)


# In[33]:


#define our search
places_result = gmaps.places_nearby(location=city_string,radius=5000, open_now=False, type='hospital')


# In[34]:


#places_result['results']
my_map3 = folium.Map(location = user_city, zoom_start = 15) 
for place in places_result['results']:
    
    try:
        hospital_loc = list(place['geometry']['location'].values())
        #rating = place['rating']
        name = place['name']
        rating_person = place['user_ratings_total']
        vicinity = place['vicinity']
        #print("---->  ",name,"  ",hospital_loc,"  ",rating,"  ",rating_person,"  ",vicinity)
        folium.Marker(hospital_loc, popup = f'Rating: {rating} \n Vicinity: {vicinity}',tooltip=name).add_to(my_map3) 
    except:
        pass
my_map3.save(" my_map1.html ")     


# In[ ]:




