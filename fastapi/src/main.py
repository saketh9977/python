from helper import get_dish_details

from fastapi import FastAPI

app = FastAPI()


@app.get("/search")
async def read_item(dish, city):
    return get_dish_details(dish, city)