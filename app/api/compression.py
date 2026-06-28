from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.api_key import verify_api_key
from app.database.session import get_db
from app.schemas.request import CompressionRequest
from app.schemas.response import CompressionResponse
from app.services.compression_service import compression_service

router = APIRouter()


@router.post("/compress", response_model=CompressionResponse)
def compress(
    request: CompressionRequest,
    client=Depends(verify_api_key),
    db: Session = Depends(get_db),
):
    return compression_service.compress(
        db=db,
        client=client,
        content=request.content,
        content_type=request.content_type,
        compression_mode=request.compression_mode,
        use_caveman=request.use_caveman,
    )