from getpass import getpass
from mysql.connector import connect, Error
from Data.data import Hosts as hosts
from Data.data import Query as query


connection = connect(host=hosts.remote,
                     user=input("input username: "),
                     password=getpass("Input password: "))


def drop_db_if_present(db_name):
    db_is_presents = False
    for db in cursor:
        # print(db)
        if db_name in db[0]:
            db_is_presents = True
    if db_is_presents:
        cursor.execute(query.drop_db)


try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query.show_db)
            drop_db_if_present(db_name='online_movie_rating')
            cursor.execute(query.create_db)
            cursor.execute(query.show_db)
            for db in cursor:
                print(db[0])
except Error as e:
    print(e)
