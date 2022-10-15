import sqlite3
from venv import create

connection = sqlite3.connect('hotel.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY, \
                nome text, estrelas real, diaria real, cidade text)"
                
create_hotel = "INSERT INTO hoteis VALUES ('alpha', 'Alpha Hotel', \
                4.3, 420.34, 'Rio de Janeiro')"

cursor.execute(create_table)
cursor.execute(create_hotel)

connection.commit()
connection.close()