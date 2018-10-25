import pyodbc
outputfileHandle = open('people.html','w',encoding = 'UTF-8')
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver='{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT top 10 * from Person.Person")
row = cursor.fetchone()
outputfileHandle.write("<html>\n"+"<head>"+"</head>")
outputfileHandle.write("<body>\n"+"<table border = 1>\n")
lst = []
while row:
    lst.append(row[4])
    print(str(row[0])+" "+ row[4]+" "+ row[6])
    row = cursor.fetchone()
ID = int(input("ID: "))
print(lst[ID])
cursor.execute('select * from Person.Person where firstname =\'' + lst[ID] + '\'')
print(cursor.fetchone())

