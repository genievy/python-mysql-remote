from getpass import getpass
from mysql.connector import connect, Error
from Data.data import Hosts as hosts
from Data.data import Query as query

connection = connect(host=hosts.remote,
                     user=input("input username: "),
                     password=getpass("Input password: "),
                     database="online_movie_rating")
try:
    select_movies_query = """
    SELECT title, collection_in_mil
    FROM movies
    WHERE collection_in_mil > 300
    ORDER BY collection_in_mil  DESC
    """
    with connection.cursor() as cursor:
        cursor.execute(select_movies_query)
        for movie in cursor.fetchall():
            print(movie)
except Error as e:
    print(e)

"""
With CONCATENATION
"""
try:
    select_movies_query = """
    SELECT CONCAT(title, " (", release_year, ")"),
          collection_in_mil
    FROM movies
    ORDER BY collection_in_mil DESC
    LIMIT 5
    """
    with connection.cursor() as cursor:
        cursor.execute(select_movies_query)
        for movie in cursor.fetchall():
            print(movie)
except Error as e:
    print(e)