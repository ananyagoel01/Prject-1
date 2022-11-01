#!/usr/bin/env python
# coding: utf-8

# In[55]:


# Import required modules
import csv
import sqlite3
import pandas as pd 
import os
import json

# Connecting to the database
connection = sqlite3.connect('/Users/ananyagoel/Desktop/DS 2002/test.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
cursor.execute('DROP TABLE IF EXISTS movie')
cursor.execute('''CREATE TABLE movie
             (rank text, release_date text, title text, url text, production_cost text, domestic_gross text, worldwide_gross text,
             opening_weekend int, mpaa text, genre text, theaters text, runtime int, year int)''')

# Opening the csv file
#file = open('/Users/ananyagoel/Desktop/DS 2002/top-500-movies.csv')
data_location = os.path.join(os.getcwd(),'/Users/ananyagoel/Desktop/DS 2002/')
data_file = os.path.join(data_location,'top-500-movies.csv')

contents_df =pd.read_csv(data_file, header=0, index_col=0)
#contents_df.head()
display (contents_df)



contents_df.to_sql('movie',connection, if_exists='replace', index=False)
#display (cursor.fetchall())

# SQL query to insert data into the
# movie table
#insert_records = "INSERT INTO movie (rank, release_date, title, url, production_cost, domestic_gross, worldwide_gross, opening_weekend,mpaa,genre, theaters,runtime,year) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"

# Importing the contents of the file
# into our movie table
#cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the movie table To
# Output to the console screen
select_all = "SELECT * FROM movie"
rows = cursor.execute(select_all).fetchall()

for row in rows:
   print(row)
    
# Committing the changes
#connection.commit()


# In[53]:


#contents_json =pd.read_csv(data_file, header=0, index_col=0)
#display (contents_json)
contents_df.to_json (r'/Users/ananyagoel/Desktop/DS 2002/new-top-500-movies.json')


# In[69]:


count_rows="SELECT COUNT(*) FROM movie"
rows=cursor.execute(count_rows)
for r in rows:
    print ('There are '+ str(r[0])+' rows in the dataset')
  


# In[71]:


count_cols="select count(*) from pragma_table_info('movie')"
cols=cursor.execute(count_cols)
for c in cols:
    print ('There are '+ str(c[0])+ ' columns in the dataset')


# In[37]:


#merging columns worldwide gross and domestic gross
select_gross="SELECT rank, title,release_date, url, production_cost, worldwide_gross||'+'|| domestic_gross,opening_weekend,mpaa,genre, theaters,runtime, year FROM movie"
total_gross=cursor.execute(select_gross).fetchall()
#prining new dataframe
for t in total_gross:
    print (t)

