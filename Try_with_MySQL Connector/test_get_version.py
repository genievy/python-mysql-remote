from mysql.connector import connect, Error
from getpass import getpass
from Data import data as data

dbconnect = connect(host=data.Hosts.remote_host,
                    port=data.Ports.user_port,  # in this one is not necessary
                    user=input("Input username: "),
                    db="mysql",
                    password=getpass("Input password: "))
cursor = dbconnect.cursor()
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
if data:
    print('Version retrieved: ', data)
else:
    print('Version not retrieved.')

dbconnect.close()
