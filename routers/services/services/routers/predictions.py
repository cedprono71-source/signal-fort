from fastapi import APIRouter, HTTPException
from services.stats import calculate_match_probabilities

router = APIRouter(prefix="/api", tags=["Predictions"])

@router.get("/predict")
def predict_match(home_expected: float, away_expected: float):
    """Calcule les probabilités d'un match via les statistiques (loi de Poisson)."""
    if home_expected < 0 or away_expected < 0:
        raise HTTPException(status_code=400, detail="Les espérances de buts doivent être positives.")

    probs = calculate_match_probabilities(home_expected, away_expected)
    return {
        "home_expected": home_expected,
        "away_expected": away_expected,
        "probabilities": probs
    }

