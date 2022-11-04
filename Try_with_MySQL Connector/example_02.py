from getpass import getpass
from mysql.connector import connect, Error
from Data import data as data

try:
    with connect(host=data.Hosts.remote_host,
                 port=data.Ports.user_port,  # in this one is not necessary
                 user=input("Input username: "),
                 password=getpass("Input password: ")) as connection:
        print(connection)
except Error as e:
    print(e)
