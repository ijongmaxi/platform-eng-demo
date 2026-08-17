from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import engine, Base, get_db
from app import models, schemas, crud

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ads Platform", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Welcome to Ads Platform API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/ads/", response_model=schemas.Ad)
def create_ad(ad: schemas.AdCreate, db: Session = Depends(get_db)):
    return crud.create_ad(db=db, ad=ad)

@app.get("/ads/", response_model=List[schemas.Ad])
def read_ads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ads = crud.get_ads(db, skip=skip, limit=limit)
    return ads

@app.get("/ads/{ad_id}", response_model=schemas.Ad)
def read_ad(ad_id: int, db: Session = Depends(get_db)):
    db_ad = crud.get_ad(db, ad_id=ad_id)
    if db_ad is None:
        raise HTTPException(status_code=404, detail="Ad not found")
    return db_ad

@app.put("/ads/{ad_id}", response_model=schemas.Ad)
def update_ad(ad_id: int, ad: schemas.AdUpdate, db: Session = Depends(get_db)):
    db_ad = crud.update_ad(db, ad_id=ad_id, ad=ad)
    if db_ad is None:
        raise HTTPException(status_code=404, detail="Ad not found")
    return db_ad

@app.delete("/ads/{ad_id}")
def delete_ad(ad_id: int, db: Session = Depends(get_db)):
    success = crud.delete_ad(db, ad_id=ad_id)
    if not success:
        raise HTTPException(status_code=404, detail="Ad not found")
    return {"message": "Ad deleted successfully"}
