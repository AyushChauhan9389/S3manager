import sqlite3

def init_db():
    conn = sqlite3.connect('gallery.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  filename TEXT UNIQUE,
                  last_modified TEXT,
                  size INTEGER)''')
    conn.commit()
    conn.close()

def get_items():
    conn = sqlite3.connect('gallery.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    items = c.fetchall()
    conn.close()
    return items

def add_item(filename, last_modified, size):
    conn = sqlite3.connect('gallery.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO items (filename, last_modified, size) VALUES (?, ?, ?)',
              (filename, last_modified, size))
    conn.commit()
    conn.close()