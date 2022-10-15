import sqlite3

connection = sqlite3.connect('hotel.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY, \
                nome text, estrelas real, diaria real, cidade text)"

cursor.execute(create_table)
connection.commit()
connection.close()