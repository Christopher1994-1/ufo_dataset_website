import datetime
import calendar
import pandas as pd

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

print(json_rows)
