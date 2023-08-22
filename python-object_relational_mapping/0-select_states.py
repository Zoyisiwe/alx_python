"""A script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_states(mysql_username, mysql_password, database_name):
    """The function that takes 3 arguments"""
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Construct the SQL query
    query = """
        SELECT * FROM states
        ORDER BY id ASC
    """

    # Execute the query
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
    

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the function to list states
    list_states(mysql_username, mysql_password, database_name)
