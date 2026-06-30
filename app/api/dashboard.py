from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.api_key import verify_api_key
from app.database.session import get_db
from app.services.dashboard_service import dashboard_service

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db),
):
    return dashboard_service.get_summary(db)


@router.get("/history")
def dashboard_history(
    db: Session = Depends(get_db),
):
    return dashboard_service.get_history(db)


@router.get("/me")
def my_dashboard(
    client=Depends(verify_api_key),
    db: Session = Depends(get_db),
):
    return dashboard_service.get_client_summary(
        db=db,
        client_id=client.id,
    )
@router.get("/today")
def today_dashboard(
    db: Session = Depends(get_db),
):
    return dashboard_service.get_today_stats(db)