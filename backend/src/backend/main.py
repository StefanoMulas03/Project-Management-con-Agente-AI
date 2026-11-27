from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from backend.core.config import settings
from backend.core.dependencies import get_db


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version
)


@app.get("/")
def root():
    return {"message": "Project Management API"}


    
@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))

    return {"database": result.scalar_one()}