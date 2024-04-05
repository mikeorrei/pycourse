import fake_api

print("List of users:")
print(fake_api.get_users())

print("Specific user:")
# print(fake_api.get_user("1111"))
# print(fake_api.get_user("5555"))
# response = fake_api.get_user("1111")
# print(response["data"])
response = fake_api.get_user("5555")
# print(response["data"]["username"])
try:
    print(response["data"]["username"])
except Exception as e:
    print(f"User data for id 5555 not found with message: {response['data']} and exception {e}")
