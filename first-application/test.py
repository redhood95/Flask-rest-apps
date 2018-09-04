# this file is just for testing how sqlite works with python

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

users = [
(2,'yose','asdfee'),
(3,'tose','asdeef'),
(4,'jrdfse','eedsdf')
]
insert_query ="INSERT INTO users VALUES (?,?,?)"
cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
