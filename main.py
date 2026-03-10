from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Marketplace AI")

# Schema for marketplace items
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float
    category: str

# Mock database
items_db = []

@app.get("/")
async def home():
    return {"status": "Online", "message": "Marketplace AI Backend is running"}

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    item.id = len(items_db) + 1
    items_db.append(item)
    return item

@app.get("/items", response_model=List[Item])
async def list_items():
    return items_db

@app.post("/ai/suggest-price")
async def suggest_price(item_description: str):
    # This is where you will later integrate a model like GPT or a regression model
    # Current logic: Simple mock suggestion based on text length
    suggested = len(item_description) * 1.25 
    return {
        "input_description": item_description,
        "suggested_price": round(max(10.0, suggested), 2),
        "currency": "USD"
    }