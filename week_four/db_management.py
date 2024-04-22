import uuid

class API():
    def __init__(self, token):
        self.token = token

class DBManagement():
    def __init__(self):
        self.data = {}

        self.api = API(token="1234")


    def add_user(self, name: str, age: int) -> dict:
        """
        Adds a new user to the DB

        Args:
            name: str, The name of the user
            age: int, The age of the user

        Returns:
            The dictionary of the user's data
        """
        user = {
            "name": name,
            "age": age
        }

        user_id = str(uuid.uuid4())

        self.data[user_id] = user
        return self.data[user_id]
    
    def get_all_users(self) -> list:
        """
        Gets all of the users from the DB

        Returns:
            A list of all the users
        """
        users = []

        for user in self.data:
            users.append(self.data[user])
        
        return users
    
    def get_user_by_id(self, user_id: str) -> (dict | None):
        """
        Gets a specific user based on their provided ID

        Args:
            user_id: str, The user ID for the user you want to query

        Returns:
            The user corresponding to the ID if they exist, None if no user is found
        """
        if user_id in self.data:
            return self.data[user_id]
        else:
            return None
        
    def get_user_by_name(self, name: str) -> (dict | None):
        """
        Get a specific user based on their name

        Args:
            name: str, The name of the user you want to query

        Returns:
            The user corresponding to the name if they exist, None if no user is found
        """
        for user in self.data:
            if self.data[user]["name"] == name:
                return self.data[user]

        return None

    def get_user_id(self, name: str) -> (str | None):
        """
        Get a specific user's ID based on their name

        Args:
            name: str, The name of the user you want to query

        Returns:
            The user ID corresponding to the name if they exist, None if no user is found
        """
        for user in self.data:
            if self.data[user]["name"] == name:
                return user
            
        return None

    def delete_user(self, user_id: str) -> bool:
        for user in self.data:
            if user == user_id:
                self.data.pop(user)
                return True
            
        return False


if __name__ == '__main__':
    db = DBManagement()

    db.add_user(name="billy", age=5)
    db.add_user(name="joe", age=3)
    db.add_user(name="bob", age=45)
    db.add_user(name="mary", age=16)
    db.add_user(name="cleetus", age=87)

    while True:
        print("Would you like to [1]get all users, [2]get user by name, [3]get user by id, [4]get a user's id, [5]add a user, [6]delete a user, [q] to quit.")
        choice = input()
        print("")

        match choice:
            case "1":
                print("Users currently in the DB:")
                print(db.get_all_users())
                print("")

            case "2":
                print("Enter the name of the user you want to get.")
                name = input()
                print("")
                print(db.get_user_by_name(name=name))
                print("")

            case "3":
                print("Enter the ID of the user you want to get.")
                user_id = input()
                print("")
                print(db.get_user_by_id(user_id=user_id))
                print("")

            case "4":
                print("Enter the name of the user to get their ID.")
                name = input()
                print("")
                print(db.get_user_id(name=name))
                print("")

            case "5":
                print("Enter the name of the user you want to add.")
                name = input()
                print("")
                print("Enter the age of the user you want to add.")
                age = input()
                
                user = db.add_user(name=name, age=age)

                print("")
                print("User added:")
                print(f"ID: {db.get_user_id(name=name)}")
                print(f"Data: {user}")
                print("")

            case "6":
                print("Enter the ID of the user you want to delete.")
                user_id = input()
                
                status = db.delete_user(user_id=user_id)
                print("")

                if status:
                    print(f"User {user_id} successfully deleted.")
                else:
                    print(f"User {user_id} not found.")

                print("")

            case "q":
                print("Goodbye")
                break

            case _:
                print("You did not provide a valid option.")
                print("")

