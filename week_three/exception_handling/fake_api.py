user_data = [
    {
        "username": "cloud",
        "email": "mike@test.com",
        "id": "1111"
    },
    {
        "username": "tifa",
        "email": "tifa@test.com",
        "id": "2222"
    },
    {
        "username": "barrett",
        "email": "barrett@test.com",
        "id": "3333"
    },
    {
        "username": "vincent",
        "email": "vincent@test.com",
        "id": "4444"
    },
]

def get_users():
    return {"code": 200, "data": user_data}


def get_user(user_id: str):
    for user in user_data:
        if user["id"] == user_id:
            return {"code": 200, "data": user}
    else:
        return {"code": 400, "data": f"user with id {user_id} not found"}
    