
# coding: utf-8

# In[16]:

# google geocode
from geopy.geocoders import GoogleV3
geolocator = GoogleV3()

API_CALL_LIMIT = 2000

import sys

if len(sys.argv) < 3:
	print >> sys.stderr, "Usage:", sys.argv[0], " <input file> <key column>"
	print >> sys.stderr, """    Note that the input file should not contain the ".csv" extension.
    If your filename is "sample_data.csv" then the first argument should
    be "sample_data". The key column is a column in your input that must be
    preserved in the output file."""
	sys.exit(1)

file_name=sys.argv[1]

input_file = open("%s.csv" % (file_name), 'r')
output_file = open("%s.coded.csv" % (file_name), 'w')
key_column = sys.argv[2]

if len(sys.argv) > 3:
	batch = int(sys.argv[3])
else:
	batch = 1

import csv
incsv = csv.DictReader(input_file, dialect="excel")
outcsv = csv.writer(output_file)

incsv.fieldnames = [x.strip().lower() for x in incsv.fieldnames]

key = key_column.strip().lower()
if not key in incsv.fieldnames:
	print >> sys.stderr, "[ERR] Cannot find key column %s in input data." % (key_column)
	sys.exit(2)

outcsv.writerow([key_column, 'Address', 'Longitude', 'Latitude'])

if batch > 1:
	print "Seeking to start of batch %d at record %d..." % (batch, (batch*API_CALL_LIMIT)-1)
	for i in range(1,(batch*API_CALL_LIMIT)-1):
		incsv.next()

api_count = 0
for row in incsv:
    address = "%s, %s, %s, %s" % (row['address'], row['city'], row['state'], row['zip'])

    try:
        address, (latitude, longitude) = geolocator.geocode(address)
        api_count += 1
    except:
        print "[ERR] FAILED TO GET LOCATION FOR ", address
    else:
        print address, longitude, latitude
        outcsv.writerow([row[key], address, longitude, latitude])

    if api_count >= API_CALL_LIMIT:
    	print "Limit of %d calls hit, stopping." % (API_CALL_LIMIT)
    	break

