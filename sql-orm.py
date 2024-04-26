#import the libraries, we do not need table anymore because with ORM we do not create tables but python classes.
#These Python classes that we'll create will subclass the declarative_base, meaning that
#any class we're making will extend from the main class within the ORM.
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base   # declarative_base class from declarative extension library

# sessionmaker class from orm library,  instead of making a connection to the database
#directly, we'll be asking for a session
from sqlalchemy.orm import sessionmaker 

#link the python file to the chinook database, through variable db I assign the pointing out to local chinook database. /// means local hosting
db = create_engine("postgresql:///chinook")

#we need a variable called 'base', which will be set to the declarative_base() class.
#This new 'base' class will essentially grab the metadata that is produced by our database
#table schema, and creates a subclass to map everything back to us here within the 'base' variable.
base= declarative_base()


# create a class-based model for the "artist" table
class artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)

# create a class-based model for the "album" table
class album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("Artist.artist_id"))

# create a class-based model for the "Track" table
class track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unit_price = Column(Float)


#Session variable will instantiate the sessionmaker() class from the ORM, making
#a new instance of the sessionmaker, and point to our 'db' engine variable in order to use
#the database
Session= sessionmaker(db)

#in order to connect to the database, we have to call Session()
#and open an actual session. To do that, we need another variable called
#'session', but this time using a lowercase 's', and we set that to equal the new instance
#of the Session() from above.
session= Session()

#The last thing we need to do before we can work with our database, is to actually create
#the database subclass and generate all metadata. The base variable, given that it's a subclass
#from the declarative_base, will now use the .create_all() method from our database metadata.
base.metadata.create_all(db)

#query 1 select everything from artist table
#let's create a new variable called 'artists', and using our existing 'session' instance, we need to use
#the .query() method to query the Artist class. That should simply select everything on the
#table within the Artist class we defined above. We then need to iterate over the results found,
#and print each of the columns using dot-notation on our for-loop.
#artists = session.query(artist)
#for artist in artists:
#    print(artist.artist_id, artist.name, sep= " | ")

#query 2 select name column from artist table
#artists = session.query(artist)
#for artist in artists:
 #   print(artist.name, sep= " | ")

#query3 select only queen from artist table
#artist = session.query(artist).filter_by(name="Queen").first()
#print(artist.artist_id, artist.name, sep= " | ")

#query4 select only artist_id = 51 from artist table
#artist = session.query(artist).filter_by(artist_id=51).first()
#print(artist.artist_id, artist.name, sep= " | ")

#query5 select only albums with artist_id = 51
albums = session.query(album).filter_by(artist_id = 51)
for album in albums:
    print (album.album_id, album.title, album.artist_id, sep = " | ")

#query6 select only tracks where composer = queen
tracks = session.query(track).filter_by(composer= "Queen")
for track in tracks:
    print (track.track_id, track.name, track.composer, sep = " | ")