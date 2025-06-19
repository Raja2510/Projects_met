from fastapi import FastAPI
from controller import router as rt
app=FastAPI()


app.include_router(rt)






