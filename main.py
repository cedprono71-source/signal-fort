from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from routers import public, admin, predictions
from database import init_db

app = FastAPI(title="Signal Fort", version="1.0.0")

# Initialisation de la base de données au démarrage
@app.on_event("startup")
def startup_event():
    init_db()

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
