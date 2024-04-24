import psycopg2  #import the library

#connect to chinook database
connection= psycopg2.connect(database="chinook")


#build a cursor object of the database, A cursor object is another way of saying a 'set' or 'list', similar to an 'array' in JavaScript.
# Essentially, anything that we query from the database will become part of this cursor object,
# and to read that data, we should iterate over the cursor using a for-loop, as an example.
cursor= connection.cursor()

#query 1
#cursor.execute('SELECT * FROM "artist"')

#query 2
#cursor.execute('SELECT "name" FROM "artist"')

#query3
#cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

#query4
#cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

#query5
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

#fetch the results (multiple) -> Before we start to query the database, we need to set up a way for our data to be retrieved,
#or fetched, from the cursor. I use fetchall() command if I need to query multiple records from database. otherwise fetchone()
results = cursor.fetchall()
#results = cursor.fetchone()

#close the connection to the database: Next, once our results have been fetched, we need to end the connection to the database,
#so the connection isn't always persistent.
connection.close()

#As previously mentioned, our data sits within a cursor object, similar to an array, so in
# order to retrieve each record individually, we need to iterate over the results using a for-loop.
for result in results:
    print(result)


