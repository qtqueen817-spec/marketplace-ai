from typing import List, Optional

# This function acts as your 'AI' pricing assistant
def calculate_suggested_price(category: str, db_items: list):
    # 1. Filter the database for items in the same category
    matching_prices = [item.price for item in db_items if item.category == category]
    
    if not matching_prices:
        return None  # Return None if we don't have enough data yet
    
    # 2. Calculate statistical markers
    avg_price = sum(matching_prices) / len(matching_prices)
    
    return {
        "suggested_price": round(avg_price, 2),
        "item_count": len(matching_prices),
        "market_high": max(matching_prices),
        "market_low": min(matching_prices)
    }