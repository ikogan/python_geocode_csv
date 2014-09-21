python_geocode_csv
==================

A python script to load and geocode csv

# Usage
To run, add an argument of the filename WITHOUT the .csv extension

    python geocode.py filename

# Output
Creates a new output file:
> filename.coded.csv

    $ python geocode.py sample_data
    401 I Street Southwest, Washington, DC 20024, USA -77.0181505 38.8796067
    3219 O Street Northwest, Washington, DC 20007, USA -77.0648106 38.9081992
    3219 O Street Northwest, Washington, DC 20007, USA -77.0648106 38.9081992
    3219 O Street Northwest, Washington, DC 20007, USA -77.0648106 38.9081992
    3219 O Street Northwest, Washington, DC 20007, USA -77.0648106 38.9081992
    3219 O Street Northwest, Washington, DC 20007, USA -77.0648106 38.9081992
    3219 O Street Northwest, Washington, DC 20007, USA -77.0648106 38.9081992
    3219 O Street Northwest, Washington, DC 20007, USA -77.0648106 38.9081992
    3219 O Street Northwest, Washington, DC 20007, USA -77.0648106 38.9081992

# Requirements
Needs the following python modules
geopy
pandas
