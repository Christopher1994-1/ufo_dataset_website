import pandas as pd
import other


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



search = "nevada"


def has_uppercase(string):
    for char in string:
        if char.isupper():
            return True
    return False




# search 'las vegas, nv'
def city_state_lower(s):
    
    # Getting the search result 
    
    #############################################################
    # indexing elements and capping and stripping it
    city = s[0].title().strip()
    state = s[1].upper().strip()
    
    # checking to see if the state and city are in the dataset
    rows = dataframe[(dataframe["state"] == state) & (dataframe['city'] == city)]
    
    json_rows = []
    for _, row in rows.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)
    
    # getting the state to add to search result, 'Nevada' from state_codes Dict
    reformed_state = other.state_codes[state]

    # getting oldest date in dataset
    rows["date"] = pd.to_datetime(rows["date"])
    oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0]

    # getting the total number of rows 
    number_of_rows = rows.shape[0]

    # search result infomation to be returned 
    search_result_para = f"Search results of {number_of_rows} rows for {city}, {reformed_state} since {oldest_date}"
    
    
    
    return search_result_para, json_rows


# search 'las vegas, nevada'
def city_state_whole(s):
    
    # indexing elements and capping and stripping it
    city = s[0].title().strip()
    state = s[1].strip()
    
    # indexing the state_names dict for value
    state = state_names[state]
    
    # checking to see if the state and city are in the dataset
    rows = dataframe[(dataframe["state"] == state) & (dataframe['city'] == city)]
    
    # getting the state to add to search result, 'Nevada' from state_codes Dict
    reformed_state = other.state_codes[state]

    # getting oldest date in dataset
    rows["date"] = pd.to_datetime(rows["date"])
    oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0]

    # getting the total number of rows 
    number_of_rows = rows.shape[0]

    # search result infomation to be returned 
    search_result_para = f"Search results of {number_of_rows} rows for {city}, {reformed_state} since {oldest_date}"
    
    return search_result_para


# search 'nv'
def just_state(s):
    
    # indexing elements and capping and stripping it
    state = str(s).strip().upper() # -> NV
    
    # indexing the state_codes dict for value
    reformed_state = state_codes[state] # -> Nevada
    
    # checking to see if the state and city are in the dataset
    rows = dataframe[(dataframe["state"] == state)]


    # getting oldest date in dataset
    rows["date"] = pd.to_datetime(rows["date"])
    oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0] # -> 1973

    # getting the total number of rows 
    number_of_rows = rows.shape[0]

    # search result infomation to be returned 
    search_result_para = f"Search results of {number_of_rows} rows for the state of {reformed_state} since {oldest_date}"
    
    return search_result_para


# search 'Nevada'
def just_state2(s):
    
    # indexing elements and capping and stripping it
    state = str(s).strip() # -> nevada
    
    #indexing the state_codes dict for value
    reformed_state = state_names[state] # -> NV
    
    # checking to see if the state and city are in the dataset
    rows = dataframe[(dataframe["state"] == reformed_state)]


    # getting oldest date in dataset
    rows["date"] = pd.to_datetime(rows["date"])
    oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0] # -> 1973

    # getting the total number of rows 
    number_of_rows = rows.shape[0]

    # search result infomation to be returned 
    search_result_para = f"Search results of {number_of_rows} rows for the state of {state.title()} since {oldest_date}"
    
    return search_result_para


# search 'nevada'
def just_state3(s):
    
    # indexing elements and capping and stripping it
    state = str(s).strip() # -> NV
    
    #indexing the state_codes dict for value
    reformed_state = state_codes[state] # -> Nevada
    
    # checking to see if the state and city are in the dataset
    rows = dataframe[(dataframe["state"] == state)]


    # getting oldest date in dataset
    rows["date"] = pd.to_datetime(rows["date"])
    oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0] # -> 1973

    # getting the total number of rows 
    number_of_rows = rows.shape[0]

    # search result infomation to be returned 
    search_result_para = f"Search results of {number_of_rows} rows for the state of {reformed_state} since {oldest_date}"
    
    return search_result_para





# checking to see if search query == 'las vegas, nv'
if search.count(','):
    query = search.split(',')
    city = query[0].title().strip()
    state = query[1].upper().strip()
    
    # checking if state == nv
    if len(state) == 2:
        search_result_info, row = city_state_lower(query)
        
        print()
        print()
        print()
        
        
    # checking if state == nevada
    else:
        # getting the state to be lowercase
        state = state.lower()
        # indexing the state from the state_names dict to gets it code
        state_to_state = state_names[state]
        # Conditional statements to check if state and city exist in dataset
        rows = dataframe[(dataframe["state"] == state_to_state) & (dataframe['city'] == city)]
        
        # Getting the search result
        search_result_info = city_state_whole(query)
    
    
        json_rows = []
        for _, row in rows.iterrows():
            json_row = row.to_dict()
            json_rows.append(json_row)
            
        # return render_template('/search/searched.html', search=search, json_rows=json_rows, search_result_info=search_result_info)
            

        
        
#checking to see search query == 'nv'
elif len(search) == 2 and search.count(',') == 0:
    new = search.upper()
    
    
    rows = dataframe[(dataframe["state"] == new)]
    
    search_result_info = just_state(new)

    json_rows = []
    for _, row in rows.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)
    
    # return render_template('/search/searched.html', search=search, json_rows=json_rows, search_result_info=search_result_info)



# checking to see ig search query == 'nevada'
elif len(search) > 3 and search.count(',') == 0:
    
    # checking if Nevada
    if has_uppercase(search):
        new = search.lower()
        
        state_co = state_names[new]
        
        rows = dataframe[(dataframe["state"] == state_co)]
        
        search_result_info = just_state2(new)

        json_rows = []
        for _, row in rows.iterrows():
            json_row = row.to_dict()
            json_rows.append(json_row)
            
        # return render_template('/search/searched.html', search=search, json_rows=json_rows, search_result_info=search_result_info)


    # else nevada
    else:
        
        new = state_names[search]
        rows = dataframe[(dataframe["state"] == new)]
        
        search_result_info = just_state3(new)

        json_rows = []
        for _, row in rows.iterrows():
            json_row = row.to_dict()
            json_rows.append(json_row)
            
        print()
        print(search_result_info)
        
        # return render_template('/search/searched.html', search=search, json_rows=json_rows, search_result_info=search_result_info)


