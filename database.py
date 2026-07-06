#database.py

import sqlite3
from datetime import datetime

DATABASE_NAME = 'ioc_tracker.db'
 
def add_ioc(ioc_type, value, source):
    """
    Adds a new IOC to the database.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    first_seen = datetime.now().isoformat()
    cursor.execute('''
    INSERT INTO indicators (type, value, first_seen, source) VALUES (?, ?, ?, ?)
    ''', (ioc_type, value, first_seen, source))
    conn.commit()
    conn.close()
    print(f'IOC added successfully: {value}')

def get_all_iocs():
    """Retrieves all IOCs from the database."""
    # The following lines must be indented
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM iocs ORDER BY first_seen DESC")
    
    rows = cursor.fetchall()
    
    conn.close()
    return rows
    