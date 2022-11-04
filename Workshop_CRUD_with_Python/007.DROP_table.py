from getpass import getpass
from mysql.connector import connect, Error
from Data.data import Hosts as hosts


connection = connect(host=hosts.remote,
                     user=input("input username: "),
                     password=getpass("Input password: "),
                     database="online_movie_rating")
try:
    with connection.cursor() as cursor:
        drop_table_query = f"DROP TABLE table_name"
        cursor.execute(drop_table_query)
        connection.commit()
except Error as e:
    print(e)
