from fastapi import FastAPI
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
fastapi ifrom fastapi import FastAPI
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
mport FastAPI
from contextlib import asynccontextmanager
import logging

from config import APP_VERSION
from database import init_db
from routers import public, admin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("signal-fort")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialisation au démarrage de l'application
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

@app.get("/")
def root():
    return {
        "app": "Signal Fort",
        "version": APP_VERSION,
        "docs_url": "/docs"
    }

