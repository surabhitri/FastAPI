from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()


@app.get("/")
async def root():
    return {
        "Message": "Please type in your name and predict what you will do after graduating from MIDS"
    }


@app.get("/predict/{str}")
async def predict(string: str):
    list = [
        "You will be the CEO of Apple! Congratulations :P",
        " will start a PhD at Duke!",
        " will run for President :P",
        " will adopt a dog!",
        " will adopt a cat. Woooo",
        " will decide to backpack across Europe!",
        " will become a professor for MIDS",
        " will start a new company!",
        " will take all of us on a trip to Disneyland!",
    ]

    random_cho = random.choice(list)
    return {string + random_cho}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
