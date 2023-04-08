import sqlite3


# Create a database connection and cursor
conn = sqlite3.connect('user_data.db')
cur = conn.cursor()

for i in cur.execute("SELECT * FROM users"):
    print(i)

# cur.execute("DELETE FROM users")

# for i in cur.execute("SELECT * FROM users"):
#     print('after')
#     print(i)


# # Create a table
# cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, location TEXT)''')

# Commit the changes and close the connection
conn.commit()
conn.close()




