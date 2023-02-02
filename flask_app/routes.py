from flask_app import app
from flask import render_template, request
import pandas as pd
import json
import datetime
import calendar


dataframe = pd.read_csv('ufo_data_nuforc.csv')
index_cap = []


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
    
    if request.method == 'POST':
        search = request.form['query']
        return render_template('index.html', search=search, json_rows=json_rows, is_index=index_cap)
    
    
        
    return render_template('index.html', json_rows=json_rows, is_index=index_cap)



# html route for search result
@app.route('/index/search', methods=["GET", "POST"])
def index_search():
    global index_cap
    if len(index_cap) >= 1:
        index_cap = []
        index_cap.append(0)
        
    return render_template('index.html', is_index=index_cap)


# html route for month clicked
@app.route('/index/month', methods=["GET", "POST"])
def index_month():
    global index_cap
    if len(index_cap) >= 1:
        index_cap = []
        index_cap.append(0)
    
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
    
    return render_template('index.html', json_rows=json_rows, is_index=index_cap)




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
    