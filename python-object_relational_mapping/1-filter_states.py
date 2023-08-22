"""A script that lists all states with a name starting
 with N (upper N) from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


def list_states_starting_with_N(mysql_username, mysql_password, database_name):
    """A function that list states with a name starting with N"""
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
        WHERE name LIKE 'N%'
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

    # Call the function to list states starting with N
    list_states_starting_with_N(mysql_username, mysql_password, database_name)
