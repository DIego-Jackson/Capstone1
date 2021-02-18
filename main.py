

import requests
import random
import mysql.connector


API_KEY = "AIzaSyCFpLxXBtbw60ezOmanixKBa8hVIGGkmLg"

'''getting the neighbourhoods from text document    ****dont uncomment until final script run*********'''
places = {}
f = open("neighborhood_list.txt", 'r')

# saving the bottom right of the geolocation to neighborhood name
for x in f:
    # places.append(x[:-1])
    address = x[:-1] + ", edmonton, AB"
    params = {
        'key': API_KEY,
        'address': address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params).json()
    # getting the lat and long
    places[x[:-1]] = {"lat_min": float(response["results"][0]["geometry"]["location"]["lat"]) - 0.003,
                      "lng_min": float(response["results"][0]["geometry"]["location"]["lng"]) + 0.003,
                      "lat_max": float(response["results"][0]["geometry"]["location"]["lat"]) + 0.003,
                      "lng_ma": float(response["results"][0]["geometry"]["location"]["lng"]) - 0.003,
                      }
    
    
# closes the file 
f.close()

print(places)
'''for testing ====================================
places = {"ABBOTTSFIELD": {"lat": 53.574732396760396, "lng": -113.38678573704114},
          "YORK": {"lat": 53.17473123123396, "lng": -113.98678586434114},
          "ALBERTA AVENUE": {"lat": 53.374732396760396, "lng": -113.78678573704114}}
========================================================'''
# connects to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password='G3%DrhG?3tR"gJM5',
    database="CMPTCAP"
)

# gets the database
mycursor = mydb.cursor()

for x in places:
    print(x)

    sql = "UPDATE NH_gps SET lat_max='"+places[x]["lat_max"]+"', lng_max='"+places[x]["lng_max"]+"', " \
          "lat_min='"+places[x]["lat_min"]+"', lng_min='"+places[x]["lng_min"]+"' WHERE NH_name='"+x+"'"
    mycursor.execute(sql)






