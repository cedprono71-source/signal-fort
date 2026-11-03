import logging
from database import db

logger = logging.getLogger("signal-fort")

def insert_sample_match(event_id: str, league: str, home_team: str, away_team: str, home_score: int, away_score: int, date: str):
    """Insère ou met à jour un match dans l'historique."""
    with db() as conn:
        conn.execute("""
            INSERT INTO matches_history (event_id, league, home_team, away_team, home_score, away_score, date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(event_id) DO UPDATE SET
                home_score = excluded.home_score,
                away_score = excluded.away_score
        """, (event_id, league, home_team, away_team, home_score, away_score, date))
    logger.info(f"Match enregistré : {home_team} vs {away_team} ({date})")

