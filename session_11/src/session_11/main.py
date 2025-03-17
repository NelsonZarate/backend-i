from fastapi import FastAPI, HTTPException
import logging

# In-memory "database" with items structured as {id: {item details}}
global items
items = {}

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the FastAPI API!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    logger.info(f"Item endpoint called for item_id: {item_id}")
    logger.info(items)
    if item_id not in items.keys():
        logger.error(f"Item with ID {item_id} not found.")
        raise HTTPException(status_code=404, detail="Item not found")
    
    item = items[item_id]
    return {"message": f"This is the items page! Item: {item}"}

@app.get("/items/")
async def read_all_items():
    logger.info("Items endpoint called")
    return {"message": f"This is the items page! All items: {items}"}

@app.post("/items/")
async def create_item(item: dict):
    logger.info(f"Item received: {item}")
    # A simple validation example
    if "name" not in item or "id" not in item:
        logger.error("Item does not contain 'name' or 'id'")
        raise HTTPException(status_code=400, detail="Item must have both 'name' and 'id'")
    
    item_id = item["id"]
    if not isinstance(item_id,int):
        logger.error("Item id must be INT")
        raise HTTPException(status_code=400, detail="Item id must be INT")
    
    if item_id in items:
        logger.error("Item id exists")
        raise HTTPException(status_code=400, detail="Item must have different 'id'")
        
    # Store the item in the dictionary with the ID as the key
    items[item_id] = item
    logger.info(f"Item with ID {item_id} created.")
    logger.info(items)
    return {"message": "Item created successfully", "item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    logger.info(f"Updating item with ID {item_id} with new data: {item}")
    
    # Simple validation
    if "name" not in item:
        logger.error("Item does not contain 'name'")
        raise HTTPException(status_code=400, detail="Item must have a name")
    
    # Check if the item exists
    if item_id not in items:
        logger.error(f"Item with ID {item_id} not found.")
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Update the item
    items[item_id] = item
    logger.info(f"Item with ID {item_id} successfully updated")
    
    return {"message": f"Item with ID {item_id} updated", "updated_item": item}

# Run the application using Uvicorn with:
# poetry run uvicorn main:app --reload
