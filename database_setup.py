#
#database_setup.py
#
#This script intializes the SQlite database and creates the "indicators" table.
#It is meant to be run once to set up the environment.

#We start by importing the sqlite3 module, which is Python's built-in library for interacting with SQLite databases.
import sqlite3

#We will need this later, but it's good practice to put imports at the top of the script.
#This module helps us get the current date and time.

def setup_database():
    """
    Connects to the database and creates the "indicators" table.
    """
#This line creates a connection to the SQLite database file "ioc_tracker.db".
#If the file does not exist, it will be created:
conn = sqlite3.connect('ioc_tracker.db')

# A cursor is an object that allows us to execute SQL commands in the database.
cursor = conn.cursor()

#Here, we define the structure of our table using a SQL command.
#The triple quotes allow us to write the command over multiple lines for readability.

#id: A unique number for each entry (Primary Key).It automatically increments with each new entry.
#type: The type of indicator (e.g., IP address, domain, hash).
#value: The actual IOC data. The UNIQUE contraint prevents duplicates.
#first_seen: The timestamp when the IOC was added.
#source: Where the analyst first found IOC (e.g firewall, email, etc).
create_table_query = """
CREATE TABLE IF NOT EXISTS indicators (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    value TEXT NOT NULL UNIQUE,
    first_seen TEXT NOT NULL,
    source TEXT 
); 
"""

#This line executes the SQL command defined above.
cursor.execute (create_table_query)

#'.commit()' is used to save the changes made to the database file.
conn.commit()

#It's best practice to close the connection to the database when you're done.
conn.close()

print("Database 'iocs.db' and table 'indicators' have been created successfully.")

#This checks if the script is being run directly (not imported as a module).If it is run directly, it will execute the 'setup_database()' function.
if __name__ == '__main__':
    setup_database() 
