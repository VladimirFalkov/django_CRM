# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysq1-connector
# pip install mysq1-connector-python

import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sharlotta2019'
)


# prepare a cursor object

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE elderco')

print("All Done, sir!")