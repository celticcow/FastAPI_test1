#!/usr/bin/python3

from fastapi import FastAPI
from fastapi import Request
import uvicorn
import requests

app = FastAPI()

@app.get("/")
async def root():
    return({'msg' : 'root'})

@app.post("/info")
async def info(info : Request):
    req_info = await info.json()
    print("here")
    print(req_info)

    output_json = {
        "status" : "success",
        "data" : req_info
    }
    return(output_json)
#end