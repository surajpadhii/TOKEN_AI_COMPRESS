from fastapi import Depends, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.api_key_service import api_key_service

api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False,
)


def verify_api_key(
    api_key: str = Security(api_key_header),
    db: Session = Depends(get_db),
):
    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key missing",
        )

    client = api_key_service.get_by_key(db, api_key)

    if client is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )

    if not client.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="API Key disabled",
        )

    return client