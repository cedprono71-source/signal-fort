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

@router.get("/matches")
def get_matches(date: str = None):
    """Récupère les matchs de la base de données, filtrés par date si demandée."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if date:
        cursor.execute("SELECT * FROM matches WHERE match_date = ?", (date,))
    else:
        cursor.execute("SELECT * FROM matches")

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]
