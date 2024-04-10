import json

from fastapi import FastAPI

from models import StoreItem


app = FastAPI()

with open("store_items.json", "r") as f:
    data = json.load(f)

items: list[StoreItem] = []

for item in data:
    items.append(StoreItem(**item))
    #items.append(StoreItem(id=item["id"], name=item["name"], description=item["description"], float=item["price"]))


@app.get("/items")
async def get_items() -> list[StoreItem]:
    return items

@app.post("/items")
async def create_items(item: StoreItem) -> None:
    items.append(item)

@app.put("/items/{item_id}")
async def update_items(item_id: int, updated_item: StoreItem) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = updated_item
            return

@app.delete("/items/{item_id}")
async def delete_items(item_id: int) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return
