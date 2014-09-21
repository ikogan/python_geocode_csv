
# coding: utf-8

# In[16]:

# google geocode
from geopy.geocoders import GoogleV3
geolocator = GoogleV3()

import sys

file_name=sys.argv[1]

input_file = "%s.csv" % (file_name)
output_file = "%s.coded.csv" % (file_name)

import pandas as pd
df = pd.read_csv(input_file)

# clean data
df=df.fillna('')
df=df.rename(columns=lambda x: x.strip())

df['latitude']=0.0
df['longitude']=0.0

for i,row in df.iterrows():
    address = "%s, %s, %s, %s" % (row['Address'], row['City'], row['State'],row['Zip'])

    try:
        address, (latitude, longitude) = geolocator.geocode(address)
    except:
        print "[ERR] FAILED TO GET LOCATION FOR ", address
    else:
        df['latitude'][i] = latitude
        df['longitude'][i] = longitude
        print address, longitude, latitude


# write geocoded data to file
print "saving to " + output_file
df.to_csv(output_file)

