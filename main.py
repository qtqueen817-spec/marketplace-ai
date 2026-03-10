@app.post("/items")
async def create_item_for_user(item: ItemCreate, current_user: User = Depends(get_current_user)):
    # The item is now tied to the logged-in user
    new_item = Item(**item.dict(), owner_id=current_user.id)
    
    # AI Logic: You can still trigger your price suggestion here!
    # suggestion = calculate_suggested_price(item.category, db_items)
    
    db.add(new_item)
    db.commit()
    return {"message": "Item posted to your profile!", "item": new_item}