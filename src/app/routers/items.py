"""Router for item operations."""

from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.item import ItemCreate, ItemResponse
from app.services.item_service import ItemService
from app.utils.auth import get_current_user

router = APIRouter()
item_service = None

@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, current_user: str = Depends(get_current_user)):
    """Create a new item."""
    return item_service.create_item(item)

@router.get("/", response_model=List[ItemResponse])
async def get_items():
    """Get all items."""
    return item_service.get_all_items()

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    """Get a specific item by ID."""
    item = item_service.get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
