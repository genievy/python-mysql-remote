from getpass import getpass
from Data import data as data
from mysql.connector import connect, Error

dbconnect = connect(host=data.Hosts.remote,
                    port=data.Ports.user_port,  # in this one is not necessary
                    user=input("Input username: "),
                    password=getpass("Input password: "),
                    db='my_shop')

cursor = dbconnect.cursor()

cursor.execute("DROP TABLE IF EXISTS MOVIE")
query = f"CREATE TABLE MOVIE(  \
          id int(11) NOT NULL,\
          name varchar(20),\
          year int(11),\
          director varchar(20),\
          genre varchar(20),\
          PRIMARY KEY (id))"

cursor.execute(query)

dbconnect.close()
