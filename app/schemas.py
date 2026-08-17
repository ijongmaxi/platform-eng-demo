from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AdBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    currency: str = "USD"
    category: str
    location: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None

class AdCreate(AdBase):
    pass

class AdUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    currency: Optional[str] = None
    category: Optional[str] = None
    location: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    is_active: Optional[bool] = None

class Ad(AdBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
