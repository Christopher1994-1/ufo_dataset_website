import datetime
import calendar
import pandas as pd
from flask_app import states
import mysql.connector


state_names = {
    'california': "CA", 
    'florida': "FL", 
    'washington': "WA", 
    'texas': "TX", 
    'new york': "NY", 
    'arizona': "AZ", 
    'pennsylvania': "PA", 
    'ohio': "OH", 
    'illinois': "IL",
    'north carolina': "NC",
    'michigan': "MI", 
    'oregon': "OR", 
    'colorado': "CO",
    'new jersey': "NJ", 
    'missouri': "MO", 
    'georgia': "GA", 
    'massachusetts': "MA", 
    'virginia': "VA", 
    'wisconsin': "WI", 
    'indiana': "IN", 
    'tennessee': "TN", 
    'south carolina': "SC", 
    'minnesota': "MN", 
    'connecticut': "CT", 
    'maryland': "MD", 
    'kentucky': "KY", 
    'nevada': "NV",
    'new mexico': 'NM', 
    'utah': "UT", 
    'oklahoma': "OK", 
    'alabama': "AL", 
    'idaho': "ID", 
    'iowa': "IA", 
    'maine': "ME", 
    'arkansas': "AR", 
    'new hampshire': "NH", 
    'kansas': "KS", 
    'louisiana': "LA", 
    'montana': "MT", 
    'west virginia': "WV", 
    'mississippi': "MS", 
    'nebraska': "NE", 
    'hawaii': "HI", 
    'alaska': "AK", 
    'vermont': "VT", 
    'rhode island': "RI", 
    'delaware': "DE", 
    'wyoming': "WY", 
    'south dakota': "SD",
    'north dakota': "ND",
    'puerto rico': "PR", 
    'virgin islands': "VI",
    
}

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



search = "las vegas, nevada"

# def has_uppercase(string):
#     for char in string:
#         if char.isupper():
#             return True
#     return False


# # search 'las vegas, nv'
# def city_state_lower(s):
#     city = s[0].title().strip()
#     state = s[1].upper().strip()
    
#     rows = dataframe[(dataframe["state"] == state) & (dataframe['city'] == city)]
#     reformed_state = states.state_codes[state]

#     rows["date"] = pd.to_datetime(rows["date"])
#     oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0]

#     number_of_rows = rows.shape[0]

#     search_result_para = f"Search results of {number_of_rows} rows for {city}, {reformed_state} since {oldest_date}"
    
#     return search_result_para


# # search 'las vegas, nevada'
# def city_state_whole(s):
#     city = s[0].title().strip()
#     state_ = s[1]
#     state = state_names[state_].upper()
    
#     rows = dataframe[(dataframe["state"] == state) & (dataframe['city'] == city)]
#     rows["date"] = pd.to_datetime(rows["date"])
#     oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0]
#     number_of_rows = rows.shape[0]
    
    
#     search_result_para = f"Search results of {number_of_rows} rows for {city}, {state} since {oldest_date}"
    
#     return search_result_para



# # checking to see if search query == 'las vegas, nv'
# if search.count(','):
#     query = search.split(',')
#     city = query[0].title().strip()
#     state = query[1].upper().strip()
    
#     # checking if state == nv
#     if len(state) == 2:
#         rows = dataframe[(dataframe["state"] == state) & (dataframe['city'] == city)]
        
#         search_result_info = city_state_lower(query)
        
#         json_rows = []
#         for _, row in rows.iterrows():
#             json_row = row.to_dict()
#             json_rows.append(json_row)
        
#         print()
#         print(search_result_info)
        
#     # checking if state == nevada
#     else:
#         state = state.lower()
#         state_to_state = state_names[state]
#         rows = dataframe[(dataframe["state"] == state_to_state) & (dataframe['city'] == city)]
        
#         search_result_info = city_state_whole(query)
        
#         json_rows = []
#         for _, row in rows.iterrows():
#             json_row = row.to_dict()
#             json_rows.append(json_row)
        
#         print()
#         print(search_result_info)
        
    

# # checking to see ig search query == 'nv'
# elif len(search) == 2 and search.count(',') == 0:
#     new = search.upper()
#     rows = dataframe[(dataframe["state"] == new)]

#     json_rows = []
#     for _, row in rows.iterrows():
#         json_row = row.to_dict()
#         json_rows.append(json_row)
        
#     print()
#     print(json_rows)
    
# # checking to see ig search query == 'nevada'
# elif len(search) > 3 and search.count(',') == 0:
#     # checking if Nevada
#     if has_uppercase(search):
#         new = search.lower()
#         state_co = state_names[new]
#         rows = dataframe[(dataframe["state"] == state_co)]

#         json_rows = []
#         for _, row in rows.iterrows():
#             json_row = row.to_dict()
#             json_rows.append(json_row)
            
#         print()
#         print(json_rows)
        
#     # else nevada
#     else:
#         new = state_names[search]
#         rows = dataframe[(dataframe["state"] == new)]

#         json_rows = []
#         for _, row in rows.iterrows():
#             json_row = row.to_dict()
#             json_rows.append(json_row)
            
#         print()
#         print(json_rows)











