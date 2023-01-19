from mysql.connector import connect
from getpass import getpass
from Data import data as data

dbconnect = connect(host=data.Hosts.remote,
                    port=data.Ports.user_port,  # in this one is not necessary
                    user=input("Input username: "),
                    password=getpass("Input password: "),
                    db="mysql")
cursor = dbconnect.cursor()
cursor.execute("SELECT User, Host  FROM  user")

data = cursor.fetchone()
print(data)

dbconnect.close()
