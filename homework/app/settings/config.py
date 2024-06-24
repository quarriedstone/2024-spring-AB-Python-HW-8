from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

pg_string = "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"
ENGINE = create_engine(pg_string)

SessionLocal = Session(ENGINE, expire_on_commit=False)


def get_db():
    """Create and get database session.

    :yield: database session.
    """
    with Session(ENGINE) as session:
        try:
            return session
        except HTTPException:
            session.rollback()
            raise
        finally:
            session.close()
