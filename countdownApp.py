import datetime

user_input=input("Enter your goal and deadline like goal:deadline(DD.MM.YYYY): ")
user_input_list=user_input.split(":")
goal=user_input_list[0]
deadline=user_input_list[1]

deadline_date=datetime.datetime.strptime(deadline,"%d.%m.%Y")
today=datetime.datetime.today()

print(f"Time left to complete {goal} is {(deadline_date - today).days} days")