from user import User
from post import Post

user1 = User("John","doe","DevOps Engineer")
user1.get_user_info()

user1.change_job_title("Senior Developer")
user1.get_user_info()


post1 = Post("Success", "GS")
post1.get_message()