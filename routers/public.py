from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Public"])

@router.get("/status")
def api_status():
    """Vérifie l'état de l'API publique."""
    return {
        "status": "online",
        "message": "Bienvenue sur l'API publique de Signal Fort."
    }

