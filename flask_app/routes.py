from flask_app import app
from flask import render_template, request
import pandas as pd
import json
import datetime
from . import states
import calendar


dataframe = pd.read_csv('ufo_data_nuforc.csv')
index_cap = []


def search_result_paragraph(s):
    city = s[0].title().strip()
    state = s[1].upper().strip()
    
    rows = dataframe[(dataframe["state"] == state) & (dataframe['city'] == city)]
    reformed_state = states.state_codes[state]

    rows["date"] = pd.to_datetime(rows["date"])
    oldest_date = str(rows["date"].min()).split(' ')[0].split('-')[0]

    number_of_rows = rows.shape[0]

    search_result_para = f"Search results of {number_of_rows} rows for {city}, {reformed_state} since {oldest_date}"
    
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
        search = request.form['query'].split(',')
        if len(search) > 1:
            city = search[0].title().strip()
            state = search[1].upper().strip()
            
            search_result_para = search_result_paragraph(search)

            rows = dataframe[(dataframe["state"] == state) & (dataframe['city'] == city)]
            
            json_rows = []
            for _, row in rows.iterrows():
                json_row = row.to_dict()
                json_rows.append(json_row)
            
            
        return render_template('/search/searched.html', 
                               search=search, 
                               json_rows=json_rows,
                               search_para=search_result_para,
                               )
    
    
    # if search query == ''
    elif request.method == 'POST':
        search = request.form['query']
        if search == '':
            rows = dataframe.head(5)
            json_rows = []
            for _, row in rows.iterrows():
                json_row = row.to_dict()
                json_rows.append(json_row)
                
        return render_template('/search/searched.html', search=search, json_rows=json_rows)
        
    
    
        
    return render_template('/search/searched.html', search=search, json_rows=json_rows)


# html route for month clicked
@app.route('/month_frame', methods=["GET", "POST"])
def index_month():
    
    date = str(datetime.datetime.now()).split(" ")[0].split('-')

    year, month, day = date
    now = f"12/{day}/{int(year[2:])-1}"

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
        st = states.state_codes[state]
        
        state_count[st] = [count, per]
    
    return render_template('/stat/stats_index.html', 
                           number_of_rows=formatted_string, 
                           merged_data=n,
                           state_dict=state_count,
    )
    



@app.route('/infomation', methods=["GET", "POST"])
def info():
    return render_template('/info/info_index.html')