from mysql.connector import connect, Error
from getpass import getpass
from Data.data import Hosts as hosts
from Data.data import Ports as ports


dbconnect = connect(host=hosts.remote,
                    port=ports.user_port,  # in this one is not necessary
                    user=input("Input username: "),
                    password=getpass("Input password: "),
                    )

cursor = dbconnect.cursor()
cursor.execute("CREATE DATABASE tools COLLATE utf8_general_ci;")
dbconnect.close()
