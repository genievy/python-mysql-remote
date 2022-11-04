from getpass import getpass
from mysql.connector import connect, Error
from Data.data import Hosts as hosts
from Data.data import Query as query
from Data.data import DataQuery as data_query


connection = connect(host=hosts.remote,
                     user=input("input username: "),
                     password=getpass("Input password: "),
                     database="online_movie_rating")
try:
    with connection.cursor() as cursor:
        cursor.executemany(query.insert_reviewers, data_query.reviewers_records)
        cursor.executemany(query.insert_ratings, data_query.ratings_records)
        connection.commit()
except Error as e:
    print(e)