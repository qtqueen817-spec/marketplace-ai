from app.services.pricing import calculate_suggested_price

@app.get("/ai/price-check/{category}")
async def get_price_suggestion(category: str):
    # In a real scenario, 'items_db' would be your SQLAlchemy query results
    result = calculate_suggested_price(category, items_db)
    
    if not result:
        return {"message": "New category detected. No pricing data available yet."}
    
    return result