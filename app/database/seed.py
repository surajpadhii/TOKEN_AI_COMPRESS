from app.database.database import SessionLocal
from app.database.models import APIKey

db = SessionLocal()

existing = (
    db.query(APIKey)
    .filter(APIKey.api_key == "sk_test_123456789")
    .first()
)

if existing:
    print("API Key already exists")
else:
    db.add(
        APIKey(
            client_name="TOKEN_AI Admin",
            api_key="sk_test_123456789",
            plan="Enterprise",
            active=True,
        )
    )

    db.commit()
    print("API Key Seeded")

db.close()