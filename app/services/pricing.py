from typing import List
from app.models import Item  # Assuming your SQLAlchemy model is named Item

def calculate_suggested_price(category: str, db_items: List[Item]):
    # Filter items that match the category
    matching_items = [item.price for item in db_items if item.category == category]
    
    if not matching_items:
        return None  # No data yet to make a suggestion
    
    # Calculate the average price
    avg_price = sum(matching_items) / len(matching_items)
    
    return {
        "suggested_price": round(avg_price, 2),
        "data_points": len(matching_items),
        "min_price": min(matching_items),
        "max_price": max(matching_items)
    }