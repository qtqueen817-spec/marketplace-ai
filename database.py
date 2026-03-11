import os
from sqlalchemy import create_url
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This URL matches the service name 'db' from your docker-compose.yaml
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/marketplace")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()