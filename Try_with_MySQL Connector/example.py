from mysql.connector import connect, Error
from Data import data as data
from getpass import getpass

connection = connect(host=data.Hosts.remote_host,
                     port=data.Ports.user_port,
                     user=input("Input username: "),
                     password=getpass("Input password: "))

with connection:  # creating a connection
    """The complete set of strings returned by an instruction is called the result set.
    Cursors is a mechanism for processing several result sets at once."""
    cursor = connection.cursor()  # Create an instance of the established connection cursor
    with cursor:  # Checking the connection to the DB
        cursor.execute("SELECT VERSION()")  # Execute the request. The resulting set is written to the cursor memory
        info = cursor.fetchone()  # The fetchone method returns one line of data.
        if info:
            print('Version retrieved: ', info)
        else:
            print('Version not retrieved.')

    # with cursor:
