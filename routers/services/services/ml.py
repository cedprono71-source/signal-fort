import os
import joblib
import logging
from sklearn.ensemble import RandomForestClassifier
from config import MODEL_PATH
from database import db

logger = logging.getLogger("signal-fort")

def train_model():
    """Entraîne un modèle simple de prédiction basé sur l'historique."""
    with db() as conn:
        rows = conn.execute("""
            SELECT home_score, away_score FROM matches_history
            WHERE home_score IS NOT NULL AND away_score IS NOT NULL
        .fetchall()

    if len(rows) < 10:
        logger.warning("Pas assez de données pour entraîner le modèle (minimum 10 matchs requis).")
        return False

    X = []
    y = []
    for r in rows:
        hs, as_ = r["home_score"], r["away_score"]
        # Exemple simple de features et target (1 = Home win, 0 = Draw, 2 = Away win)
        X.append([hs + as_, abs(hs - as_)])
        if hs > as_:
            y.append(1)
        elif hs == as_:
            y.append(0)
        else:
            y.append(2)

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    logger.info("Modèle ML entraîné et sauvegardé avec succès.")
    return True

