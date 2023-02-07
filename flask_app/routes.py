from flask_app import app
from flask import render_template, request, redirect, session, Flask
import pandas as pd
import json
import datetime
import calendar
import mysql.connector


# app = Flask(__name__)

dataframe = pd.read_csv('ufo_data_nuforc.csv')
# dataframe = pd.read_csv('/home/cejkirk/mysite/ufo_data_nuforc.csv') and on line 472 in month_frame function
index_cap = []

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





def has_uppercase(string):
    for char in string:
        if char.isupper():
            return True
    return False



########################## Search result functions ##########################


# search 'las vegas, nv'
def city_state_lower(s):
    
    # Getting the search result 
    
    #############################################################
    # indexing elements and capping and stripping it
    city = s[0].title().strip()
    state = s[1].upper().strip()
    
    # checking to see if the state and city are in the dataset
    rows = dataframe[(dataframe["state"] == state) & (dataframe['city'] == city)]
    
    
    # getting the state to add to search result, 'Nevada' from state_codes Dict
    reformed_state = state_codes[state]

    # getting oldest date in dataset
    rows["date"] = pd.to_datetime(rows["date"])
    oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0]

    # getting the total number of rows 
    number_of_rows = rows.shape[0]

    # search result infomation to be returned 
    search_result_para = f"Search results of {number_of_rows} rows for {city}, {reformed_state} since {oldest_date}"
    
    
    
    return search_result_para


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
    reformed_state = state_codes[state]

    # getting oldest date in dataset
    rows["date"] = pd.to_datetime(rows["date"])
    oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0]

    # getting the total number of rows 
    number_of_rows = rows.shape[0]

    # search result infomation to be returned 
    search_result_para = f"Search results of {number_of_rows} rows for {city}, {reformed_state} since {oldest_date}"
    
    return search_result_para


# search 'nevada'
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







# base index html route
@app.route('/', methods=["GET", "POST"])
def index():
    global index_cap
    if len(index_cap) >= 1:
        index_cap.append(1)
        
    rows = dataframe.head(5)
    json_rows = []
    for _, row in rows.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)
    
    
        
    return render_template('index.html', json_rows=json_rows, is_index=index_cap)


# html route for when a user signs up
@app.route('/index/sign_up', methods=["POST", "GET"])
def index_sign_up():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        location = request.form['loc']
        session['name'] = name
        session['email'] = email
        session['location'] = location
        
        # code here to add user info to a database and call first_email function
        
    return redirect('/index/confirmation_sign_up_success')





# html route for sign up confirmation html page
@app.route('/index/confirmation_sign_up_success')
def confirmation():
    name = session.get('name')
    email = session.get('email')
    location = session.get('location')
    return render_template('confirmation.html', name=name, email=email, location=location)


# html route for search result
@app.route('/index/search', methods=["GET", "POST"])
def index_search():
    rows = dataframe.head(5)
    json_rows = []
    for _, row in rows.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)
    
    
    # if search query == 'something'
    if request.method == 'POST':
        search = request.form['query']
        
        if search != '':
            value = 1
        
        # checking to see if search query == 'las vegas, nv'
        if search.count(','):
            query = search.split(',')
            city = query[0].title().strip()
            state = query[1].upper().strip()
        
            # checking if state == nv
            if len(state) == 2:
                value = 0 # value == 0, 0 issues
                # getting the return result for string 
                search_result_info = city_state_lower(query)
                
                rows_row = dataframe[(dataframe["state"] == state) & (dataframe['city'] == city)]
    
    
                json_rows = []
                for _, row in rows_row.iterrows():
                    json_row = row.to_dict()
                    json_rows.append(json_row)
                
                return render_template('/search/searched.html', value=value, search=search, json_rows=json_rows, search_result_info=search_result_info)
            
            
            # checking if state == nevada
            else:
                value = 0 # value == 0, 0 issues
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
                    
                return render_template('/search/searched.html', value=value, search=search, json_rows=json_rows, search_result_info=search_result_info)
            
    
        #checking to see search query == 'nv'
        elif len(search) == 2 and search.count(',') == 0:
            new = search.upper()
            value = 0 # value == 0, 0 issues
            
            
            rows = dataframe[(dataframe["state"] == new)]
            
            search_result_info = just_state(new)

            json_rows = []
            for _, row in rows.iterrows():
                json_row = row.to_dict()
                json_rows.append(json_row)
            
            return render_template('/search/searched.html', value=value, search=search, json_rows=json_rows, search_result_info=search_result_info)
        
        
        # checking to see ig search query == 'nevada'
        elif len(search) > 3 and search.count(',') == 0:
            
            # checking if Nevada
            if has_uppercase(search):
                value = 0 # value == 0, 0 issues
                new = search.lower()
                
                state_co = state_names[new]
                
                rows = dataframe[(dataframe["state"] == state_co)]
                
                search_result_info = just_state2(new)

                json_rows = []
                for _, row in rows.iterrows():
                    json_row = row.to_dict()
                    json_rows.append(json_row)
                    
                return render_template('/search/searched.html', value=value, search=search, json_rows=json_rows, search_result_info=search_result_info)


            # checking if nevada
            elif search in state_names.keys():
                value = 0 # value == 0, 0 issues
                new = state_names[search]
                rows = dataframe[(dataframe["state"] == new)]
                
                search_result_info = just_state3(new)

                json_rows = []
                for _, row in rows.iterrows():
                    json_row = row.to_dict()
                    json_rows.append(json_row)

        
                return render_template('/search/searched.html', value=value, search=search, json_rows=json_rows, search_result_info=search_result_info)

    
        return render_template('/search/searched.html', value=value, search=search, json_rows=json_rows)



# html route for month clicked
@app.route('/month_frame', methods=["GET", "POST"])
def index_month():
    
    date = str(datetime.datetime.now()).split(" ")[0].split('-')

    year, month, day = date

    month = 12 # latest month to be updated
    year = 22 # latest year to be updated

    days = calendar.monthrange(year, month)
    days = days[1]

    month_days = []

    for i in range(1, days + 1):
        if i < 10:
            month_days.append(f"{month}/0{i}/{year}")
        else:
            month_days.append(f"{month}/{i}/{year}")

    dataframe = pd.read_csv('ufo_data_nuforc.csv')
    # dataframe = pd.read_csv('/home/cejkirk/mysite/ufo_data_nuforc.csv')


    rows = dataframe[(dataframe["date"].isin(month_days))]

    json_rows = []
    for _, row in rows.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)
    
    return render_template('/month/month_index.html', json_rows=json_rows, is_index=index_cap)




# html route for the latest a tag clicked
@app.route('/lastest_index', methods=["GET", "POST"])
def index_lasted():
    global index_cap
    if len(index_cap) >= 1:
        index_cap = []
        index_cap.append(0)
        
    rows = dataframe.head(5)
    json_rows = []
    for _, row in rows.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)

    return render_template('/latest/latest_index.html', json_rows=json_rows, is_index=index_cap)






# html route for the statistics a tag clicked
@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    number_of_rows = str(dataframe.shape[0])
    formatted_string = "{:,}".format(int(number_of_rows))
    
    
    view = dataframe['shape'].value_counts()
    new = view.to_dict()

    # for the shape of ufo
    merged_data = {}
    for key, value in new.items():
        lower_key = key.lower()
        if lower_key in merged_data:
            merged_data[lower_key] += value
        else:
            merged_data[lower_key] = value 
    n = {}
    for key1, value1 in merged_data.items():
        v = str(int(value1) / int(number_of_rows) * 100)
        v = v[:4] + "%"
        n[key1] = [value1, v]
        
        
    # for the state percentage
    state_count = {}
    changing = dataframe['state'].value_counts()
    n_dict = changing.to_dict()
    for state, count in n_dict.items():
        per = str(int(count) / int(number_of_rows) * 100)
        per = per[:4] + "%"
        st = state_codes[state]
        
        state_count[st] = [count, per]
    
    return render_template('/stat/stats_index.html', 
                           number_of_rows=formatted_string, 
                           merged_data=n,
                           state_dict=state_count,
    )
    





# route for the info link 
@app.route('/infomation', methods=["GET", "POST"])
def info():
    return render_template('/info/info_index.html')






# route for the web page 'about'
@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template('about.html')








# route for the web page 'contact'
@app.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template('contact.html')



# route for the web function 'contact_submit'
@app.route('/contact_submit', methods=["GET", "POST"])
def contact_submit():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Connect to the database
        # cnx = mysql.connector.connect(
        # host="localhost",
        # user="root",
        # password="passw0rd0098",
        # database="ufo_data"
        # )
        
    return render_template('contact_submit.html', 
                           name=name,
                           email=email,
                           message=message
        )
    
    
    



@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


