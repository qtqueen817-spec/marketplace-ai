from app.services.ai_logic import predict_category

@app.post("/items")
async def create_item(item: Item):
    # AI Logic: Auto-categorize if the user didn't provide one
    if not item.category or item.category == "string":
        item.category = predict_category(item.description)
    
    item.id = len(items_db) + 1
    items_db.append(item)
    return {
        "message": "Item listed!",
        "ai_suggested_category": item.category,
        "item": item
    }