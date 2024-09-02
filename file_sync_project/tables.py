import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')  # Replace with your database file
cursor = conn.cursor()

# Query to get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results
tables = cursor.fetchall()

# Print the list of tables
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()
