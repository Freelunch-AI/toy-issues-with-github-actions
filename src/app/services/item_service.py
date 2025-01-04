"""Service for managing item operations."""

from app.schemas.item import ItemCreate, ItemResponse
from typing import List, Optional

class ItemService:
    """Service for handling item CRUD operations."""

    def __init__(self):
        """Initialize empty items list."""
        self.items = []
        self.counter = 1

    def create_item(self, item: ItemCreate) -> ItemResponse:
        """
        Create a new item.
        
        Args:
            item: Item data for creation
            
        Returns:
            ItemResponse: Created item with ID
        """
        item_dict = item.model_dump()
        item_dict["id"] = self.counter
        item_dict["owner_id"] = 1
        self.counter += 1
        self.items.append(item_dict)
        return ItemResponse(**item_dict)

    def get_all_items(self) -> List[ItemResponse]:
        """Get all items in the system."""
        return [ItemResponse(**item) for item in self.items]

    def get_item_by_id(self, item_id: int) -> Optional[ItemResponse]:
        """
        Get item by ID.
        
        Args:
            item_id: ID of the item to retrieve
            
        Returns:
            Optional[ItemResponse]: Item if found, None otherwise
        """
        for item in self.items:
            if item["id"] == item_id:
                return ItemResponse(**item)
        return None