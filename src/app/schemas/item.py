"""Item schemas for request and response models."""

from pydantic import BaseModel, ConfigDict
from typing import Optional

class ItemBase(BaseModel):
    """Base schema for items."""
    title: str
    description: Optional[str] = None
    price: float

class ItemCreate(ItemBase):
    """Schema for creating a new item."""
    pass

class ItemResponse(ItemBase):
    """Schema for item response including database fields."""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    owner_id: int