from fastapi import APIRouter

from models.user import User
from config.db import conn, db
from schemas.user import serializeDict, serializeList   
from bson import ObjectId

user = APIRouter()

@user.get('/')
async def find_all_users():
    for i in db.users.find():
        print(i)
    print(serializeList(db.users.find()))
    return serializeList(db.users.find())

@user.get('/{id}')
async def get_user_by_id(id):
    return serializeDict(db.users.find_one({"_id": ObjectId(id)}))

@user.post('/')
async def create_user(user : User):
    db.users.insert_one(dict(user))
    print(serializeList(db.users.find()))
    return serializeList(db.users.find())

@user.put('/{id}')
async def update_user(id, user : User):
    db.users.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return serializeDict(db.users.find_one({"_id": ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return serializeDict(db.users.find_one_and_delete({"_id": ObjectId(id)}))