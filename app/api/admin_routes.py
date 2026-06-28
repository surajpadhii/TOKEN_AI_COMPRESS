from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.api_key import APIKeyCreate, APIKeyResponse
from app.services.api_key_service import api_key_service

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.post(
    "/keys",
    response_model=APIKeyResponse,
)
def create_api_key(
    request: APIKeyCreate,
    db: Session = Depends(get_db),
):
    return api_key_service.create_key(
        db=db,
        client_name=request.client_name,
        plan=request.plan,
    )


@router.get(
    "/keys",
    response_model=List[APIKeyResponse],
)
def list_keys(
    db: Session = Depends(get_db),
):
    return api_key_service.list_keys(db)


@router.put("/keys/{key_id}/disable")
def disable_key(
    key_id: int,
    db: Session = Depends(get_db),
):
    api_key_service.disable_key(db, key_id)

    return {
        "message": "API Key Disabled"
    }


@router.put("/keys/{key_id}/enable")
def enable_key(
    key_id: int,
    db: Session = Depends(get_db),
):
    api_key_service.enable_key(db, key_id)

    return {
        "message": "API Key Enabled"
    }
@router.delete("/keys/{key_id}")
def delete_key(
    key_id: int,
    db: Session = Depends(get_db),
):
    deleted = api_key_service.delete_key(
        db,
        key_id,
    )

    if not deleted:
        return {
            "message": "Client not found"
        }

    return {
        "message": "API Key Deleted"
    }