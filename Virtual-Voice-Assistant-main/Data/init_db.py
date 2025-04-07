import sqlite3

# Connect to the database (this will create it if it doesn't exist)
conn = sqlite3.connect('chats.db')

# Create a cursor object
cursor = conn.cursor()

# Create the chats table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database initialized successfully!") 