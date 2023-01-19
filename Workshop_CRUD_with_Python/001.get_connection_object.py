from getpass import getpass
from mysql.connector import connect, Error
from Data.data import Hosts as hosts
from Data import data as data

connection = connect(host=data.Hosts.remote,
                     port=data.Ports.user_port,
                     user=input("Input username: "),
                     password=getpass("Input password: "))

try:
    with connection:
        print(connection)
except Error as e:
    print(e)

