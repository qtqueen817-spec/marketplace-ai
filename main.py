from app.services.vision import identify_item_from_image
from app.services.pricing import calculate_suggested_price

@app.post("/items/smart-list") # type: ignore
async def smart_list_item(file: UploadFile = File (...), current_user: User = Depends(get_current_user)): # type: ignore
    # 1. AI identifies the item
    category = identify_item_from_image(file.file)
    
    # 2. AI suggests a price based on category
    pricing_data = calculate_suggested_price(category, items_db) # type: ignore
    
    return {
        "detected_category": category,
        "suggested_price": pricing_data["suggested_price"] if pricing_data else 10.0,
        "user": current_user.username
    }