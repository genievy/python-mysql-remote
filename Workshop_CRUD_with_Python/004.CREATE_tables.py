"""
Defining the database schema
Let's start by creating a database schema for the movie rating system. The database will consist of three tables:

1. movies:  == general information about movies ==
id
title
release year
genre
collection_in_mi

2. reviewers:  == information about people who have published movie reviews==
id
first_name
last_name

3. ratings:  == information about how these people rated the movie  ==
movie_id (foreign key)
reviewer_id (foreign key)
rating

img_url https://media.proglib.io/posts/2021/01/06/e014e591f361c06cfafcc8b5a582f013.png
"""

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
        cursor.execute(query.create_movies_table)
        cursor.execute(query.create_reviewers_table)
        cursor.execute(query.create_ratings_table)
        connection.commit()
except Error as e:
    print(e)




