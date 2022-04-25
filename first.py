
from fastapi import FastAPI,Path,HTTPException,status
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    brand:Optional[str]=None
    price:float


class UpadateItem(BaseModel):
    name:Optional[str]=None
    brand:Optional[str]=None
    price:Optional[float]=None


app=FastAPI()

@app.get("/")
def home():
    return {"data":"hello world"}


items={
    1:{
        'name':'milk',
        'brand':'milma',
        'price':29
    }
}



@app.get("/item/{item_id}")
def get_item(item_id: int=Path(None,description="Example demo")):
    if item_id  in items:
        return items[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/get_item")
def get_item(name:str=None):
    for item_id in items:
        if items[item_id]["name"]==name:
            return items[item_id]
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.get("/items")
def get_all_items():
    return items     

@app.post("/create_item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in items:
        raise HTTPException(status_code=400,detail='id alreafy exists')
    items[item_id]=item
    return items[item_id]


@app.put("/update_item/{item_id}")
def update_item(item_id:int,update_item:UpadateItem):
    if item_id not in items:
        return{'error':'id already exists'}
   
    items[item_id].update(update_item)
    return items[item_id]

@app.delete("/delete_item")
def delete_item(item_id:int):
    if item_id not in items:
        return {'error':'Not found'}
    del items[item_id]
