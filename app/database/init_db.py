from app.database.database import Base, engine
from app.database.models import APIKey

Base.metadata.create_all(bind=engine)

print("Database Initialized")