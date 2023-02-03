import datetime
import calendar
import pandas as pd

state_codes = {
    'CA': "California", 
    'FL': "Florida", 
    'WA': "Washington", 
    'TX': "Texas", 
    'NY': "New York", 
    'AZ': "Arizona", 
    'PA': "Pennsylvania", 
    'OH': "Ohio", 
    'IL': "Illinois",
    'NC': "North Carolina",
    'MI': "Michigan", 
    'OR': "Oregon", 
    'CO': "Colorado",
    'NJ': "New Jersey", 
    'MO': "Missouri", 
    'GA': "Georgia", 
    'MA': "Massachusetts", 
    'VA': "Virginia", 
    'WI': "Wisconsin", 
    'IN': "Indiana", 
    'TN': "Tennessee", 
    'SC': "South Carolina", 
    'MN': "Minnesota", 
    'CT': "Connecticut", 
    'MD': "Maryland", 
    'KY': "Kentucky", 
    'NV': "Nevada",
    'NM': 'New Mexico', 
    'UT': "Utah", 
    'OK': "Oklahoma", 
    'AL': "Alabama", 
    'ID': "Idaho", 
    'IA': "Iowa", 
    'ME': "Maine", 
    'AR': "Arkansas", 
    'NH': "New Hampshire", 
    'KS': "Kansas", 
    'LA': "Louisiana", 
    'MT': "Montana", 
    'WV': "West Virginia", 
    'MS': "Mississippi", 
    'NE': "Nebraska", 
    'HI': "Hawaii", 
    'AK': "Alaska", 
    'VT': "Vermont", 
    'RI': "Rhode Island", 
    'DE': "Delaware", 
    'WY': "Wyoming", 
    'SD': "South Dakota",
    'ND': "North Dakota",
    'DC': "Washington, DC", 
    'PR': "Puerto Rico", 
    'VI': "Virgin Islands",
}



dataframe = pd.read_csv('ufo_data_nuforc.csv')
number_of_rows = dataframe.shape[0]


view = dataframe['duration'].value_counts(dropna=True).head(40)

# TODO add a total sighting for month of etc 

print(view)



    
    














