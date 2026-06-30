from datetime import datetime
import uuid

from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def error_response(
    request: Request,
    status_code: int,
    message: str,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": {
                "code": status_code,
                "message": message,
            },
            "request_id": getattr(
                request.state,
                "request_id",
                str(uuid.uuid4()),
            ),
            "timestamp": datetime.utcnow().isoformat(),
        },
    )


async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):
    return error_response(
        request,
        exc.status_code,
        exc.detail,
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return error_response(
        request,
        422,
        "Validation Error",
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    return error_response(
        request,
        500,
        "Internal Server Error",
    )