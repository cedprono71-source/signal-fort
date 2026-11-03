import sqlite3
from database import DB_NAME

def ingest_sample_data():
    """Insère des données de test dans la base de données."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Création de la table si elle n'existe pas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            home_team TEXT,
            away_team TEXT,
            home_goals INTEGER,
            away_goals INTEGER
        )
    """)

    # Insertion de quelques matchs d'exemple
    sample_matches = [
        ("Equipe A", "Equipe B", 2, 1),
        ("Equipe C", "Equipe D", 0, 0),
        ("Equipe A", "Equipe C", 1, 3),
        ("Equipe B", "Equipe D", 2, 2)
    ]

    cursor.executemany("""
        INSERT INTO matches (home_team, away_team, home_goals, away_goals)
        VALUES (?, ?, ?, ?)
    """, sample_matches)

    conn.commit()
    conn.close()

