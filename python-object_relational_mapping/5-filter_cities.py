""" a script that takes in the name of a state as an argument
 and lists all specified items in the database"""


import MySQLdb
import sys


def list_cities_by_state(mysql_username, mysql_password,
                         database_name, state_name):
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

    # Construct the SQL query using parameterized query and user input
    query = """
        SELECT cities.id, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the query with the state name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to list cities by state
    list_cities_by_state(mysql_username, mysql_password,
                         database_name, state_name)
