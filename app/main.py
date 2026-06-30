from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError

from app.ai.headroom_client import headroom_client
from app.api.admin_routes import router as admin_router
from app.api.compression import router as compression_router
from app.api.dashboard import router as dashboard_router
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler,
)
from app.middleware.request_id import RequestIDMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

# Middleware
app.add_middleware(RequestIDMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # React
        "http://localhost:5173",      # Vite
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Exception Handlers
app.add_exception_handler(
    HTTPException,
    http_exception_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

# Startup
@app.on_event("startup")
def startup():
    print("Loading Headroom model...")
    headroom_client.preload()
    print("Model Ready")

# Routers
app.include_router(
    compression_router,
    prefix="/v1",
)

app.include_router(
    dashboard_router,
    prefix="/v1",
)

app.include_router(
    admin_router,
    prefix="/v1",
)

# Root
# ----------------------------
# Root
# ----------------------------

@app.get("/v1")
def root():
    return {
        "success": True,
        "message": "TOKEN_AI API Running",
        "version": settings.VERSION,
    }


# ----------------------------
# Health
# ----------------------------

@app.get("/v1/health")
def health():
    return {
        "status": "healthy",
        "model": "loaded",
        "version": settings.VERSION,
    }