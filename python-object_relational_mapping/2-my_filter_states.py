"""a script that takes in an argument and displays all values"""


import MySQLdb
import sys


def search_state_by_name(mysql_username, mysql_password,
                        database_name, search_name):
    """A function that takes arguments (4)"""
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

    # Construct the SQL query using format and user input
    query = """
        SELECT * FROM states
        WHERE name = '{}'
        ORDER BY id ASC
    """.format(search_name)

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
    # Get MySQL credentials and search name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    search_name = sys.argv[4]

    # Call the function to search for the state by name
    search_state_by_name(mysql_username, mysql_password,
                        database_name, search_name)
