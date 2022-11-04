from getpass import getpass
from mysql.connector import connect, Error
from Data.data import Hosts as hosts
from Data.data import Query as query

connection = connect(host=hosts.remote,
                     user=input("input username: "),
                     password=getpass("Input password: "),
                     database="online_movie_rating")
try:
    with connection.cursor() as cursor:
        alter_table_query = """
        ALTER TABLE movies
        MODIFY COLUMN collection_in_mil DECIMAL(4,1)
        """
        cursor.execute(alter_table_query)
        cursor.execute(query.show_table_movies)
        result = cursor.fetchall()
        for row in result:
            print(row)
        connection.commit()
except Error as e:
    print(e)
