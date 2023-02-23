from typing import Union

from fastapi import FastAPI

from Data import Item

app = FastAPI()

@app.get("/Wolrd")
def read_root():
    return {"Hello": "World"}

@app.get("/Item/{id}")
def read_Item(num : int):
    for itemCurrent in Item.items:
        if  itemCurrent.id == num:
            return  {"Item en cours": itemCurrent}
        else:
            print ("not exist")
        break

@app.post("/Item/create")
def create_Item(name: str, age: int, address : str, mail : str):
    itemCurrent = Item(name, age, address, mail)
    Item.items = {itemCurrent}

@app.post("/Item/{id}/modify")
def modify_Item(num : int):
    for itemCurrent in Item.items:
        if  itemCurrent.id == num:
            print ("...")
        break

@app.post("/Item/{id}/delete")
def suppr_Item(num : int):
    for itemCurrent in Item.items:
        if  itemCurrent.id == num:
            print ("Supprimer {itemCurrent.name} ?")
        else:
            print ("not exist")
        break
