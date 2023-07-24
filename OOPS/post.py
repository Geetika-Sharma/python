class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author
    
    def get_message(self):
        print(f"Message by author {self.author}: {self.message}")