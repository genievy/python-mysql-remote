from getpass import getpass
from mysql.connector import connect, Error
from Data.data import Hosts as hosts

try:
    with connect(host=hosts.remote,
                 user="ozen",
                 password="Q1!werty") as connection:
        print(connection)
except Error as e:
    print(e)

