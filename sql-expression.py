#import the libraries
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

#link the python file to the chinook database, through variable db I assign the pointing out to local chinook database. /// means local hosting
db = create_engine("postgresql:///chinook")

#The MetaData class will contain a collection of our table objects, and the associated data within those objects.
meta= MetaData(db)

#create variable for artist table, provide the name of the table = artist and meta schema = meta
artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer,primary_key=True),
    Column("name", String)
)

#create variable for album table, provide the name of the table = album and meta schema = meta
album_table = Table(
    "album", meta,
    Column("album_id", Integer,primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id"))
)

#create variable for track table, provide the name of the table = track and meta schema = meta
track_table = Table(
    "track", meta,
    Column("track_id", Integer,primary_key=True),
    Column("name", Integer),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("media_type_id", Integer, primary_key= False),
    Column("genre_id", Integer, primary_key= False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float)
)

#Now, we need to actually connect to the database, using the .connect() method, and the Python with-statement. This saves our connection to the database into a variable called 'connection'.
with db.connect() as connection:
    #query1
    #select_query = artist_table.select()

    #query2
    #select_query = artist_table.select().with_only_columns([artist_table.c.name])

    #query3
    #select_query = artist_table.select().where(artist_table.c.name=="Queen")

    #query4
    #select_query = artist_table.select().where(artist_table.c.artist_id=="51")

    #query5
    #select_query = album_table.select().where(album_table.c.artist_id=="51")

    #query6
    select_query = track_table.select().where(track_table.c.composer=="Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)

