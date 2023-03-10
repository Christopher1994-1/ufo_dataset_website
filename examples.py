import pandas as pd
import numpy as np
import sys
import matplotlib
import json



# Dataset complied from files from the National UFO Reporting Center

dataframe = pd.read_csv('ufo_data_nuforc.csv')


# print(dataframe['summary'])



# Pull out a row 
# rows = dataframe.head(5)
# json_rows = []
# for _, row in rows.iterrows():
#     json_row = row.to_dict()
#     json_rows.append(json_row)
import datetime
import calendar

current_month = datetime.datetime.now().month
current_year = datetime.datetime.now().year

if current_month == 1:
    prev_month = 12
    prev_year = current_year - 1
elif current_month == 2:
    prev_month = 12
    prev_year = current_year

# start_date = f"{prev_month}/01/{prev_year[2:]}"
# end_date = f"{prev_month}/{calendar.monthrange(prev_year, prev_month)[1]}/{prev_year[2:]}"
start_date = "12/01/22"
end_date = "12/31/22"


rows = dataframe[(dataframe["date"] >= start_date) & (dataframe["date"] <= end_date)]
json_rows = []
for _, row in rows.iterrows():
    json_row = row.to_dict()
    json_rows.append(json_row)
print(json_rows)
"""Name: summary, Length: 117829, dtype: object
posted                                          12/22/22
date                                            12/21/22
time                                            21:33:00
city                                            Columbus
state                                                 OH
shape                                              Light
duration                                     1-2 minutes
summary     4-5 orange balls of light in a straight line
images                                               NaN
Name: 1, dtype: object
"""

# for thing in json_rows:
#     print(thing['date'])







# Describe a specific column
# view = dataframe['city'].describe()

"""
count      117829
unique      20899
top       Phoenix
freq          721
Name: city, dtype: object

"""
# print(view)





# Count Distinct Values - Descending
# view = dataframe['shape'].value_counts()

"""
Light        25169
Circle       13093
Triangle     11291
Fireball      8727
Unknown       8420
Other         8327
Sphere        7993
Disk          6526
Oval          5224
Formation     4144
Changing      3269
Cigar         2958
Rectangle     2171
Flash         2107
Cylinder      1992
Diamond       1760
Chevron       1458
Teardrop      1048
Egg           1017
Cone           479
Cross          415
Star            78
Name: shape, dtype: int64
"""
# print(view)




# Get Relative Frequency - Percentage
# view = dataframe['shape'].value_counts(normalize=True)

# get value and * 100
"""
Light        0.213606
Circle       0.111119
Triangle     0.095825
Fireball     0.074065
Unknown      0.071459
Other        0.070670
Sphere       0.067836
Disk         0.055385
Oval         0.044335
Formation    0.035170
Changing     0.027744
Cigar        0.025104
Rectangle    0.018425
Flash        0.017882
"""


# print(view[0] * 100)







