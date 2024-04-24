from models.user import CreateUser, UserResponseList
from db.base import SessionLocal
from .model import User

def addUserToDB(user: CreateUser) -> User:
    with SessionLocal() as db:
        dbUser = User(
            name = user.name,
            email = user.email,
            province = user.province,
            city =  user.city,
            major = user.major
        )
        db.add(dbUser)
        db.commit()
        db.refresh(dbUser)
        return dbUser

def getUser(id:int) -> User:
    with SessionLocal() as db:
        return db.query(User).filter(User.id == id).first()


def searchUser(major:str = None, prov: str = None, city: str = None) -> UserResponseList:
    with SessionLocal() as db:
        query = db.query(User)

        if major:
            query = query.filter(User.major == major)
        
        if prov:
            query = query.filter(User.province == prov)

        if city:
            query = query.filter(User.city == city)
        return query.all()

def deleteUserFromDB(user):
    with SessionLocal() as db:
        db.delete(user)
        db.commit()