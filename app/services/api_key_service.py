import secrets

from sqlalchemy.orm import Session

from app.database.models import APIKey


class APIKeyService:

    def get_by_key(
        self,
        db: Session,
        api_key: str,
    ):
        return (
            db.query(APIKey)
            .filter(APIKey.api_key == api_key)
            .first()
        )

    def create_key(
        self,
        db: Session,
        client_name: str,
        plan: str,
    ):
        key = "sk-" + secrets.token_urlsafe(24)

        client = APIKey(
            client_name=client_name,
            api_key=key,
            plan=plan,
            active=True,
        )

        db.add(client)
        db.commit()
        db.refresh(client)

        return client

    def list_keys(
        self,
        db: Session,
    ):
        return db.query(APIKey).all()

    def disable_key(
        self,
        db: Session,
        key_id: int,
    ):
        client = (
            db.query(APIKey)
            .filter(APIKey.id == key_id)
            .first()
        )

        if client:
            client.active = False
            db.commit()

    def enable_key(
        self,
        db: Session,
        key_id: int,
    ):
        client = (
            db.query(APIKey)
            .filter(APIKey.id == key_id)
            .first()
        )

        if client:
            client.active = True
            db.commit()

    def delete_key(
        self,
        db: Session,
        key_id: int,
    ):
        client = (
            db.query(APIKey)
            .filter(APIKey.id == key_id)
            .first()
        )

        if client is None:
            return False

        db.delete(client)
        db.commit()

        return True


api_key_service = APIKeyService()