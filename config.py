import os
from zoneinfo import ZoneInfo

APP_VERSION = "33.0"
DB_PATH = os.getenv("FOOTBALL_DB_PATH", "football_history.db")
MODEL_PATH = os.getenv("MODEL_PATH", "ml_model.joblib")
PARIS_TZ = ZoneInfo("Europe/Paris")

LEAGUES = {
    "eng.1": "Premier League",
    "eng.2": "EFL Championship",
    "esp.1": "La Liga",
    "esp.2": "Segunda División",
    "ita.1": "Serie A",
    "ita.2": "Serie B",
    "ger.1": "Bundesliga",
    "ger.2": "2. Bundesliga",
    "fra.1": "Ligue 1",
    "fra.2": "Ligue 2",
    "ned.1": "Eredivisie",
    "por.1": "Liga Portugal",
    "bel.1": "Jupiler Pro League",
    "tur.1": "Süper Lig",
    "sco.1": "Scottish Premiership",
    "uefa.champions": "UEFA Champions League",
    "uefa.europa": "UEFA Europa League",
    "uefa.conf": "UEFA Conference League",
}

FD_COMPETITIONS = {
    "PL": "eng.1", "ELC": "eng.2", "PD": "esp.1", "SA": "ita.1", "BL1": "ger.1",
    "FL1": "fra.1", "DED": "ned.1", "PPL": "por.1", "CL": "uefa.champions",
}

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

