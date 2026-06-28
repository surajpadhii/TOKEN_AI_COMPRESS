from fastapi import FastAPI

from app.api.compression import router as compression_router
from app.api.dashboard import router as dashboard_router
from app.ai.headroom_client import headroom_client
from app.core.config import settings
from app.api.admin_routes import router as admin_router
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)


@app.on_event("startup")
def startup():
    print("Loading Headroom model...")
    headroom_client.preload()
    print("Model Ready")


app.include_router(compression_router)
app.include_router(dashboard_router)
app.include_router(admin_router)


@app.get("/")
def root():
    return {"message": "Headroom API Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}