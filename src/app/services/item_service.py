"""
Service for managing item operations.
"""

from app.schemas.item import ItemCreate, ItemResponse
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


class ItemService:
    """
    Service for handling item CRUD operations.
    """

    def __init__(self):
        """
        Initialize empty items list.
        """
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
        try:
            item_dict = item.model_dump()
            item_dict["id"] = self.counter
            item_dict["owner_id"] = 1
            self.counter += 1
            self.items.append(item_dict)
            return ItemResponse(**item_dict)
        except Exception as e:
            logger.exception("Error creating item: %s", e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def get_all_items(self) -> List[ItemResponse]:
        """
        Get all items in the system.
        """
        try:
            return [ItemResponse(**item) for item in self.items]
        except Exception as e:
            logger.exception("Error getting items: %s", e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def get_item_by_id(self, item_id: int) -> Optional[ItemResponse]:
        """
        Get item by ID.

        Args:
            item_id: ID of the item to retrieve

        Returns:
            Optional[ItemResponse]: Item if found, None otherwise
        """
        try:
            for item in self.items:
                if item["id"] == item_id:
                    return ItemResponse(**item)
            return None
        except Exception as e:
            logger.exception("Error getting item by ID: %s", e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
