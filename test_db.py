import os
from sqlalchemy import create_engine

# Pulls from your .env or defaults to the docker service name
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/marketplace")

def test_connection():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            print("✅ Success! The app is talking to the database.")
    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    test_connection()