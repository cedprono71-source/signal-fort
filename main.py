from ffrom fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from routers import public, admin, predictions
from database import init_db

app = FastAPI(title="Signal Fort", version="1.0.0")

# Initialisation de la base de données au démarrage
@app.on_event("startup")
on_startup = lambda: init_db()

# Montage du dossier static pour le design
app.mount("/static", StaticFiles(directory="static"), name="static")

# Inclusion des routeurs
app.include_router(public.router)
app.include_router(admin.router)
app.include_router(predictions.router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    """Affiche la page d'accueil visuelle."""
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "<h1>Bienvenue sur Signal Fort</h1><p>API opérationnelle. Rendez-vous sur <a href='/docs'>/docs</a></p>"
astapi import FastAPI
from contextlib import asynccontextmanager
import logging

from config import APP_VERSION
from database import init_db
from routers import public, admin, predictions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("signal-fort")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Démarrage de Signal Fort...")
    init_db()
    yield
    logger.info("Arrêt de l'application.")

app = FastAPI(
    title="Signal Fort API",
    version=APP_VERSION,
    lifespan=lifespan
)

# Inclusion des routeurs
app.include_router(public.router)
app.include_router(admin.router)
app.include_router(predictions.router)

@app.get("/")
def root():
    return {
        "app": "Signal Fort",
        "version": APP_VERSION,
        "docs_url": "/docs"
    }


