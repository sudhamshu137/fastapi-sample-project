def userEntitiy(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": str(item["name"]),
        "email": str(item["email"]),
        "password": str(item["password"])
    }

def usersEntity(entity) -> list:
    return [userEntitiy(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'}, **{i:a[i] for i in a if i!='_id'}}

def serializeList(a) -> list:
    return [serializeDict(i) for i in a]