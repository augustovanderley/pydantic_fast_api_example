from pydantic import BaseModel, validator
from typing import Dict
import functools

class ItemType(BaseModel):
    name: str
    can_trade: bool

class Item(BaseModel):
    name: str
    amt: int
    item_type: ItemType

    @validator("amt")
    def check_amt_limit(cls, v):
        if v > 100:
            raise ValueError("Cannot have more than 100 amount of an item")
        return v

        
class Inventory(BaseModel):
    """ This is a character's inventory """
    items: Dict[str, Item]

def main():
    food_type = ItemType(
        name="food",
        can_trade=True,
    )
    item1 = Item(
        name="Apple",
        amt=150,
        item_type=food_type
    )
    item2 = Item(
        name="Banana",
        amt=50,
        item_type=food_type
    )
    inventory = Inventory(
        items={"1": item1, "2": item2}
    )
    print(inventory.items["1"].item_type.can_trade)
    
    inventory = {
        "items": {
            "1": {
                "name": "Orange",
                "amt": 5,
                "item_type": {
                    "name": "food",
                    "can_trade": False
                }
            }
        }  
    }
    inventory2 = Inventory(**inventory)
    print(inventory2.dict())
    
if __name__ == "__main__":
    main()