from fastapi import FastAPI

app = FastAPI()

@app.get("/endpoint1")
async def endpoint1():
    return {"message": "This is endpoint 1"}

@app.get("/endpoint2")
async def endpoint2():
    return {"message": "This is endpoint 2"}

@app.get("/endpoint3")
async def endpoint3():
    return {"message": "This is endpoint 3"}
