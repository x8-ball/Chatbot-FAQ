import sqlite3
db = sqlite3.connect('mydb')
# Get a cursor object
cursor = db.cursor()
def createTable():
	cursor.execute('''
	    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
	                       phone TEXT, email TEXT unique, password TEXT)
	''')
	db.commit()
def insertUser():
	name1 = 'Andres'
	phone1 = '3366858'
	email1 = 'user@example.com'
	# A very secure password
	password1 = '12345'
	 
	name2 = 'John'
	phone2 = '5557241'
	email2 = 'johndoe@example.com'
	password2 = 'abcdef'
	 
	# Insert user 1
	cursor.execute('''INSERT INTO users(name, phone, email, password)
	                  VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
	print('First user inserted')
	 
	# Insert user 2
	cursor.execute('''INSERT INTO users(name, phone, email, password)
	                  VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
	print('Second user inserted')
	 
	db.commit()
def printTable():
	cursor.execute('''SELECT * FROM users''')

	#user1 = cursor.fetchone() #retrieve the first row
	#print(user1[0]) #Print the first column retrieved(user's name)
	all_rows = cursor.fetchall()
	for row in all_rows:
	    # row[0] returns the first column in the query (name), row[1] returns email column.
	    print(row)

printTable()