import sqlite3
from contextlib import contextmanager
import logging
from config import DB_PATH

logger = logging.getLogger("signal-fort")

def db_connect():
    conn = sqlite3.connect(DB_PATH, timeout=20, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=20000")
    return conn

@contextmanager
def db():
    """Connexion avec commit/rollback ET fermeture automatique."""
    conn = db_connect()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    with db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS matches_history (
                event_id TEXT PRIMARY KEY,
                league TEXT,
                home_team TEXT NOT NULL,
                away_team TEXT NOT NULL,
                home_score INTEGER,
                away_score INTEGER,
                date TEXT NOT NULL,
                home_id TEXT,
                away_id TEXT
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_matches_date ON matches_history(date)")
    logger.info("Base de données initialisée avec succès.")

