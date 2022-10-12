#SQL to Pandas DataFrame(with examples)
#Азитрмицин 500
#Азитромицин 250
#Индапамид 2.5
#ИТРАКОНАЗОЛ 100
#ЛЕВОФЛОКСАЦИН 500
#Лоперамид 10
#НИФУРОКСАЗИД  100 №30
#НИФУРОКСАЗИД  200 №20
#Омепразол 30
#Пироксикам 10
#Пироксикам 20
#Флуконазол 150
#Флуконазол 50
#Флуоксетин
#
import sqlite3
#Here is the complete script to create the database and table in Python:

import sqlite3
import pandas as pd
import openpyxl
import subprocess
from openpyxl.styles import Border, Side
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.styles import NamedStyle, Font, Border, Side


conn = sqlite3.connect('test_database')
c = conn.cursor()

# c.execute('''
#           CREATE TABLE IF NOT EXISTS products
#           ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)
#           ''')
#
# c.execute('''
#           INSERT INTO products (product_id, product_name, price)
#
#                 VALUES
#                 (1,'Computer',800),
#                 (2,'Printer',200),
#                 (3,'Tablet',300),
#                 (4,'Desk',450),
#                 (5,'Chair',150)
#           ''')
#
# conn.commit()

####################################################
#Step2: Get from SQL to Pandas DataFrame Now you should be able to get
#from SQL to Pandas DataFrame using pd.read_sql_query:


conn = sqlite3.connect('Pcsparse.db')

sql_query = pd.read_sql_query('''
                               SELECT
                               *
                               FROM PCSparse
                               ''', conn)

df = pd.DataFrame(sql_query, columns=['PCS_id', 'PCS_time_print', 'PCS_kod_start', 'PCS_kod_stop', 'PCS_time_print', 'Parent_name_file', 'Parent_kalibr', 'Parent_kog_group', 'PCS_file_dir', 'PCS_file_name'])#['product_id', 'product_name', 'price'])
print(df)
with pd.ExcelWriter('pandas_to_excel.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1')
#    df2.to_excel(writer, sheet_name='sheet2')
#    dframe.to_excel(writer, sheet_name='sheet_dframe')

subprocess.Popen(('start', 'pandas_to_excel.xlsx'), shell=True)


#Alternatively, you may use the approach below to get from SQL to a DataFrame:

# conn = sqlite3.connect('test_database')
# c = conn.cursor()
#
# c.execute('''
#           SELECT
#           *
#           FROM products
#           ''')
#
# df = pd.DataFrame(c.fetchall(), columns=['product_id', 'product_name', 'price'])
# print(df)

#######################################################

#Putting everything together:

#
# conn = sqlite3.connect('Pcsparse.db')
# c = conn.cursor()
#
# File "C:\Python3\Python310\lib\site-packages\pandas\core\internals\construction.py", line 985, in _finalize_columns_and_data
#     raise ValueError(err) from err
# ValueError: 6 columns passed, passed data had 19 columns
#
# c.execute('''
#           SELECT
#           *
#           FROM PCSparse
#           ''')
#
# df = pd.DataFrame(c.fetchall(), columns=['PCS_id', 'PCS_time_print', 'PCS_kod_start', 'PCS_kod_stop', 'PCS_time_print', 'PCS_context',  ])
#
# with pd.ExcelWriter('pandas_to_excel.xlsx') as writer:
#     df.to_excel(writer, sheet_name='sheet1')
# #    df2.to_excel(writer, sheet_name='sheet2')
# #    dframe.to_excel(writer, sheet_name='sheet_dframe')
#
# subprocess.Popen(('start', 'pandas_to_excel.xlsx'), shell=True)

#max_price = df['price'].max()
#print(max_price)

