from app.services.pricing import calculate_suggested_price

@app.get("/items/price-check/{category}")
async def get_price_suggestion(category: str):
    # In a real app, you'd fetch this from the DB: db.query(Item).all()
    suggestion = calculate_suggested_price(category, items_db)
    
    if not suggestion:
        return {"message": "Not enough data for this category yet."}
        
    return suggestion