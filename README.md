python_geocode_csv
==================

A python script to load and geocode csv

# Usage
To run, add an argument of the filename WITHOUT the .csv extension

    python geocode.py filename "keycolumn"

The key column is currently required and will be output as part of the
CSV. This allows easily associating the result with the original data.

# Format
The input format must contain the columns:

- Address
- City
- State
- Zip

A header for the columns is required and must match those above though
it is not case sensitive. Additionally, a "key column" must be specified.
The column will be added as the first column in the result. Note that
while the "Address" column could be the key column, if it is, two columns
with the same header (though possibly different data) will be added to the
result.

# Output
Creates a new output file:
> filename.coded.csv

    $ python geocode.py sample_data "Household ID"
    Household ID,Address,Longitude,Latitude
    0000000001,"401 I Street Southwest, Washington, DC 20024, USA",-77.01815049999999,38.8796067
    0000000002,"3219 O Street Northwest, Washington, DC 20007, USA",-77.0648106,38.90819920000001
    0000000002,"3219 O Street Northwest, Washington, DC 20007, USA",-77.0648106,38.90819920000001
    0000000002,"3219 O Street Northwest, Washington, DC 20007, USA",-77.0648106,38.90819920000001
    0000000002,"3219 O Street Northwest, Washington, DC 20007, USA",-77.0648106,38.90819920000001
    0000000002,"3219 O Street Northwest, Washington, DC 20007, USA",-77.0648106,38.90819920000001
    0000000002,"3219 O Street Northwest, Washington, DC 20007, USA",-77.0648106,38.90819920000001
    0000000002,"3219 O Street Northwest, Washington, DC 20007, USA",-77.0648106,38.90819920000001


# Requirements
Needs the "geopy" Python module. This can be installed in Ubuntu with

    sudo apt-get install python-geopy
