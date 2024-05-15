import sqlite3
import pandas as pd

import chardet

rawdata = open('02_BD_colaboradores.csv', 'rb').read()
result = chardet.detect(rawdata)
encoding = result['encoding']

with open('02_BD_colaboradores.csv', 'r', encoding=encoding) as file:
    file_content = file.read()
file_content = file_content.replace(';', ',')
with open('02_BD_colaboradores.csv', 'w', encoding=encoding) as file:
    file.write(file_content)
with open('01_BD_Absentismo.csv', 'r', encoding=encoding) as file:
    file_content = file.read()
file_content = file_content.replace(';', ',')
with open('01_BD_Absentismo.csv', 'w', encoding=encoding) as file:
    file.write(file_content)
    
df = pd.read_csv('02_BD_colaboradores.csv', encoding=encoding)
df2 = pd.read_csv('01_BD_Absentismo.csv', encoding=encoding)
conn = sqlite3.connect('db.sqlite3')
df.to_sql('colaboradores', conn, if_exists='replace', index=False)
df2.to_sql('absentismo', conn, if_exists='replace', index=False)

cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
for table in tables:
	table_content = pd.read_sql_query(f"SELECT * from {table[0]}", conn)
	print(f"Table {table[0]}:")
	print(table_content)
	print("\n")

conn.close()