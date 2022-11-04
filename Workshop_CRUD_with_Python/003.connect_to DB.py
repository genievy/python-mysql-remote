from getpass import getpass
from mysql.connector import connect, Error
from Data.data import Hosts as hosts


connection = connect(host=hosts.remote,
                     user=input("input username: "),
                     password=getpass("Input password: "),
                     database="online_movie_rating")

try:
    with connection:
        cursor = connection.cursor()
        print(connection)
except Error as e:
    print(e)
