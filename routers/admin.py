from fastapi import APIRouter
from services.ingestion import ingest_sample_data
from services.ml import train_model

router = APIRouter(prefix="/api/admin", tags=["Admin"])

@router.post("/ingest")
def trigger_ingestion():
    """Simule l'ingestion de données de matchs."""
    ingest_sample_data()
    return {"message": "Données ingérées avec succès."}

@router.post("/train")
def trigger_training():
    """Lance l'entraînement du modèle de Machine Learning."""
    result = train_model()
    return result

