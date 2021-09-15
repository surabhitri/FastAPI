from fastapi import FastAPI
import uvicorn
import random
import twint
import pandas as pd
import nest_asyncio

app = FastAPI()


@app.get("/")
async def root():
    return {
        "Message": "Please type in your name and predict what you will do after graduating from MIDS"
    }


@app.get("/tweet/{str1}")
async def tweet(str1: str):
    str2 = str1.replace("_"," ")
    nest_asyncio.apply()
    c = twint.Config()
    c.Search = [str2]       # topic
    c.Limit = 5      # number of Tweets to scrape
    # c.Store_csv = True       # store tweets in a csv file
    #c.Output = "taylor_swift_tweets.csv"     # path to csv file
    #df = pd.read_csv('taylor_swift_tweets.csv')
    # print(df)
    # c.Store_json = True
    # c.Output = "custom_out.json"
    twint.run.Search(c)


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
