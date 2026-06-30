from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.plans import PLAN_LIMITS
from app.services.usage_service import usage_service


class PlanService:

    def validate_mode(
        self,
        client,
        compression_mode,
    ):
        plan = PLAN_LIMITS.get(client.plan)

        if plan is None:
            raise HTTPException(
                status_code=403,
                detail="Unknown subscription plan.",
            )

        if compression_mode.value not in plan["allowed_modes"]:
            raise HTTPException(
                status_code=403,
                detail=f"{compression_mode.value} mode is not available for {client.plan} plan.",
            )

    def validate_daily_limit(
        self,
        db: Session,
        client,
    ):
        plan = PLAN_LIMITS[client.plan]

        limit = plan["daily_requests"]

        if limit is None:
            return

        used = usage_service.today_requests(
            db,
            client.id,
        )

        if used >= limit:
            raise HTTPException(
                status_code=429,
                detail="Daily request limit exceeded.",
            )
    def validate_rate_limit(
    self,
    db: Session,
    client,
):
        plan = PLAN_LIMITS[client.plan]

        limit = plan["requests_per_minute"]

        if limit is None:
            return

        used = usage_service.last_minute_requests(
            db,
            client.id,
        )

        if used >= limit:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Please wait a minute.",
            )

plan_service = PlanService()