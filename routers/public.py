from fastapi import APIRouter
from database import db

router = APIRouter(tags=["Public"])

@router.get("/health")
def health():
    with db() as conn:
        count = conn.execute("SELECT COUNT(*) FROM matches_history").fetchone()[0]
        teams = conn.execute("SELECT COUNT(*) FROM teams").fetchone()[0] if conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='teams'"
        ).fetchone() else 0
    return {
        "status": "ok",
        "historical_matches": count,
        "known_teams": teams,
    }

@router.get("/api/history")
def history(limit: int = 50):
    limit = max(1, min(limit, 500))
    with db() as conn:
        rows = conn.execute("""
            SELECT event_id, league, home_team, away_team, home_score, away_score, date
            FROM matches_history ORDER BY date DESC LIMIT ?
        """, (limit,)).fetchall()
    return {"count": len(rows), "matches": [dict(r) for r in rows]}

