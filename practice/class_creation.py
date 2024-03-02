class user:
    def __init__(self, user_id, user_name, followers):
        self.id = user_id
        self.name = user_name
        self.followers = 0

user1 = user("001", "Namith", "0")
print(user1.id)