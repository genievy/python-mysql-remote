from mysql.connector import connect, Error
from Data.data import Hosts as hosts
from Data.data import Query as query
from getpass import getpass


connection = connect(host=hosts.remote,
                     user=input("input username: "),
                     password=getpass("Input password: "),
                     database="online_movie_rating")
try:
    with connection.cursor() as cursor:
        data_limit = (2, 5,)
        cursor.execute(query.select_movies_limit, data_limit)
        # result = cursor.fetchall()
        # result = cursor.fetchmany(size=5)
        print(cursor.fetchone())
        print(cursor.fetchone())
        # for row in result:
        #     print(row)
except Error as e:
    print(e)

# try:
#     with connection.cursor() as cursor:
#         tables = "`release_year`",
#         cursor.execute(query.select_movies_tables, tables)
#         result = cursor.fetchall()
#         for row in result:
#             print(row)
# except Error as e:
#     print(e)
