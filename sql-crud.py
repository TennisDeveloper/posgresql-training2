#import the libraries, we do not need table anymore because with ORM we do not create tables but python classes.
#These Python classes that we'll create will subclass the declarative_base, meaning that
#any class we're making will extend from the main class within the ORM.
from sqlalchemy import (
    create_engine, Column, Integer, String
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



#create class-based model for programmer table
class Programmer(base):
    __tablename__="Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


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


#Now that our table schema is decided, we can start to add new records onto this table.
#For each new record we add, we'll assign it to a variable using the programmer's name
#as the actual variable. 

ada_lovelace= Programmer (
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"

)

alan_turing= Programmer (
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"

)

grace_hopper= Programmer (
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL language"
)

margaret_hamilton= Programmer (
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates= Programmer (
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee= Programmer (
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)

barbora_fabianova= Programmer (
    first_name = "Barbora",
    last_name = "Fabianova",
    gender = "F",
    nationality = "Slovakian",
    famous_for = "Code Institute"
)

#add each instance of the programmer to our session
#session.add(ada_lovelace)
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margaret_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_lee)
#session.add(barbora_fabianova)


#commit the session to the database
#session.commit()

#updating a single record. I am querying a single record (.first()) therefore I do not need for loop to query the database
#programmer = session.query(Programmer).filter_by(id = 7).first()
#programmer.famous_for = "World President"

#commit the session to the database
#session.commit()

#updating multiple records
#people = session.query(Programmer)
#for person in people:
#    if person.gender == "F":
#         person.gender = "Female"
#    elif person.gender == "M":
#         person.gender = "Male"
#    else:
#         print("Gender not defined")
#    session.commit()

#deleting a single record
fname = input("Enter first name: ")
lname = input("Enter last name: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name= lname).first()

if programmer is not None:
    print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
    confirmation= input("Are you sure to delete the record? (y/n)")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted.")
    else:
        print("Programmer not deleted.")
else:
    print("No records found.")


# delete multiple/all records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


#query the database to find all programmers
programmers= session.query(Programmer)
for programmer in programmers:
        print( 
            programmer.id,
            programmer.first_name + " " + programmer.last_name,
            programmer.gender,
            programmer.nationality,
            programmer.famous_for,
            sep = " | "
        )