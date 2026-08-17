from sqlalchemy.orm import Session
from app import models, schemas

def get_ads(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Ad).offset(skip).limit(limit).all()

def get_ad(db: Session, ad_id: int):
    return db.query(models.Ad).filter(models.Ad.id == ad_id).first()

def create_ad(db: Session, ad: schemas.AdCreate):
    db_ad = models.Ad(**ad.model_dump())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def update_ad(db: Session, ad_id: int, ad: schemas.AdUpdate):
    db_ad = get_ad(db, ad_id)
    if db_ad:
        update_data = ad.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_ad, key, value)
        db.commit()
        db.refresh(db_ad)
    return db_ad

def delete_ad(db: Session, ad_id: int):
    db_ad = get_ad(db, ad_id)
    if db_ad:
        db.delete(db_ad)
        db.commit()
        return True
    return False
