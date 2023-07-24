class User:
    def __init__(self, username, password, job_title):
        self.name = username
        self.password = password
        self.job_title = job_title
        
    def update_password(self, new_password):
        self.password = new_password
    
    def change_job_title(self, new_title):
        self.job_title = new_title
    
    def get_user_info(self):
        print(f"User {self.name} currently works as {self.job_title}")

