import sqlite3

DB_NAME = "signal_fort.db"

def init_db():
    """Initialise la base de données SQLite en mode WAL."""
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.close()

