from fastapi import APIRouter, Header, HTTPException, status
from config import ADMIN_TOKEN
from database import db

router = APIRouter(prefix="/admin", tags=["Admin"])

def verify_admin(x_admin_token: str = Header(None)):
    if not ADMIN_TOKEN or x_admin_token != ADMIN_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token administrateur invalide ou manquant"
        )

@router.post("/reset-db")
def reset_database(x_admin_token: str = Header(None)):
    verify_admin(x_admin_token)
    with db() as conn:
        conn.execute("DROP TABLE IF EXISTS matches_history")
    from database import init_db
    init_db()
    return {"status": "success", "message": "Base de données réinitialisée avec succès."}

