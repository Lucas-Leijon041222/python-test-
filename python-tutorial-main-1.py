import json
user_db_file = "user_database.json"

def user_exists(username):
    with open(user_db_file, "r") as file:
        users = json.load(file)
        return username in users

    def register_user(username, password):
        with open(user_db_file, "r") as file:
            users = json.load(file)

    if not user_exists(username):
        users[username] = {"password": password}

        with open(user_db_file, "w") as file:
            json.dump(users, file)

        print("User registered successfully!")
    else:
        print("User already exists. Try a different username.")

        def login():
            username = input("Enter your username: ")
            password = input("Enter your password: ")

    with open(user_db_file, "r") as file:
        users = json.load(file)

    if user_exists(username):
        if users[username]["password"] == password:
            print("Login successful!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("User not found. Please register.")

        while True:
            print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        new_username = input("Enter a new username: ")
        new_password = input("Enter a password: ")
        register_user(new_username, new_password)
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
