from fastapi import FastAPI, Request, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from db.crud import (addUserToDB, getUser, searchUser, deleteUserFromDB)
from models.user import CreateUser, UserResponse

__version__ = "0.1"

app = FastAPI(
    title="searchEngine API",
    version=__version__,
    docs_url='/docs',
    redoc_url='/redoc'
)

@app.get("/")
def get_root():
    return {"message": "Hello World! This thing is working :D"} 

@app.get("/get_user")
def get_user(id:int) -> UserResponse:
    dbuser = getUser(id)
    if dbuser == None:
        raise HTTPException(status_code=404, detail="Not Found")
    else:
        dbuser = UserResponse.from_orm(dbuser)
        return dbuser

@app.get("/search")
def search(prov: str = None, city:str = None, major:str = None):
    result = searchUser(prov=prov, city=city, major=major)
    if result == []:
        raise HTTPException(status_code=404, detail="Not Found")
    else:
        return result

@app.post("/add", status_code=201)
def add_user(userInfo: CreateUser) -> UserResponse:
    dbUser = addUserToDB(userInfo)
    dbuser = UserResponse.from_orm(dbUser)

    

    return dbuser

@app.delete("/delete", status_code=200)
def delete_user(userID:int) -> dict:
    user = getUser(userID)
    if deleteUserFromDB(user):
        return {"message": "successful"}
    else:
        raise HTTPException(status_code=404, detail="Not Found")

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = {}
    for error in exc.errors():
        details[error["loc"][-1]] = error.get("msg")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": details}),
    )