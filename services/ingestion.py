import sqlite3
from datetime import datetime, timedelta
from database import DB_NAME

def ingest_sample_data():
    """Insère un calendrier complet de matchs pour toute la saison dans la base de données."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Création de la table avec la colonne match_date (format YYYY-MM-DD)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_date TEXT,
            home_team TEXT,
            away_team TEXT,
            home_goals INTEGER,
            away_goals INTEGER,
            status TEXT DEFAULT 'FT'
        )
    """)
    
    # Sécurité au cas où la table existait déjà sans la colonne date
    try:
        cursor.execute("ALTER TABLE matches ADD COLUMN match_date TEXT")
    except sqlite3.OperationalError:
        pass

    # Nettoyage des anciennes données pour repartir sur un calendrier propre
    cursor.execute("DELETE FROM matches")

    # Liste d'équipes prestigieuses pour alimenter le calendrier
    teams = [
        ("Paris SG", "Marseille"), 
        ("Real Madrid", "FC Barcelone"), 
        ("Manchester City", "Liverpool"), 
        ("Bayern Munich", "Dortmund"),
        ("Juventus", "Inter Milan"), 
        ("Arsenal", "Chelsea"),
        ("AC Milan", "Napoli"), 
        ("Atletico Madrid", "Séville")
    ]

    # Génération d'un calendrier sur une large période (de 30 jours dans le passé à 90 jours dans le futur)
    base_date = datetime.now() - timedelta(days=30)
    season_matches = []

    for i in range(120):
        current_date = base_date + timedelta(days=i)
        date_str = current_date.strftime("%Y-%m-%d")
        
        # Associer des affiches à cette date
        t1 = teams[i % len(teams)]
        t2 = teams[(i + 3) % len(teams)]
        
        if t1 != t2:
            home_goals = (i * 7) % 4
            away_goals = (i * 3) % 4
            status = "FT" if current_date < datetime.now() else "NS"
            season_matches.append((date_str, t1[0], t1[1], home_goals, away_goals, status))

    cursor.executemany("""
        INSERT INTO matches (match_date, home_team, away_team, home_goals, away_goals, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, season_matches)

    conn.commit()
    conn.close()
