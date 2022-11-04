from mysql.connector import connect, Error
from getpass import getpass
from Data import data

dbconnect = connect(host=data.Hosts.remote_host,
                    port=data.Ports.user_port,  # in this one is not necessary
                    user=input("Input username: "),
                    password=getpass("Input password: "))

cursor = dbconnect.cursor()
director = input('Input director`s name: ')
query = f'insert into movie(id, name, year, director, genre)  \
       values (2, "Bruce Almighty", 2003, "{director}", "Comedy")'
print(query)
try:
    cursor.execute(query)
    dbconnect.commit()
except:
    dbconnect.rollback()
finally:
    dbconnect.close()
