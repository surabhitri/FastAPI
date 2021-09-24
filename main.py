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
        "Message": "Search Twitter!"
    }


@app.get("/tweet/{str1}")
async def tweet(str1: str):
    str2 = str1.replace("_"," ")
    nest_asyncio.apply()
    c = twint.Config()
    c.Search = [str2]       # topic
    c.Limit = 100      # number of Tweets to scrape
    c.Lang = "en"
    #c.Since = "2019–04–29"
    #c.Until = "2020–04–29"
    # c.Store_csv = True       # store tweets in a csv file
    # c.Output = "/FastAPI/taylor_swift_tweets.csv"     # path to csv file
    # df = pd.read_csv('/FastAPI/taylor_swift_tweets.csv')
    # print(df)
    c.Store_json = True
    c.Output = "custom_out.json"
    twint.run.Search(c)
    data=pd.read_json("custom_out.json", lines=True)
    return {"Tweet": data["tweet"] + '\n'}
    
    
    
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
