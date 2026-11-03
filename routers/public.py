from fastapi import APIRouter
import sqlite3
from database import DB_NAME

router = APIRouter(prefix="/api", tags=["Public"])

@router.get("/status")
def api_status():
    """Vérifie l'état de l'API publique."""
    return {
        "status": "online",
        "message": "Bienvenue sur l'API publique de Signal Fort."
    }

@router.get("/matches/foot")
def get_foot_matches(date: str = None):
    """Récupère les matchs de football pour une date donnée."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if date:
        cursor.execute("SELECT * FROM matches WHERE match_date = ?", (date,))
    else:
        cursor.execute("SELECT * FROM matches")

    rows = cursor.fetchall()
    conn.close()

    matches_list = []
    for row in rows:
        keys = row.keys()
        match_status = row["status"] if "status" in keys else "FT"
        match_date = row["match_date"] if "match_date" in keys else ""

        matches_list.append({
            "event_id": row["id"],
            "match_date": match_date,
            "league": "Championnat Pro",
            "home_team": row["home_team"],
            "away_team": row["away_team"],
            "home_score": row["home_goals"],
            "away_score": row["away_goals"],
            "game_state": match_status,
            "home_logo": "",
            "away_logo": ""
        })

    return {"matches": matches_list}
