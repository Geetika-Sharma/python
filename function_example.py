calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {calculation_to_units*num_of_days} hours"



def validate_and_execute():
    if number.isdigit():
        input_number = int(number)
        if input_number > 0:
            print(days_to_units(input_number))
        elif input_number == 0:
            print("You entered 0")
    else:
        print("Invalid Input")

def try_except_validate(days):
    try:
        input_number = int(days)
        if input_number > 0:
            print(days_to_units(input_number))
        elif input_number == 0:
            print("You entered 0")
        else:
            print("-ve number")
    except ValueError:
        print("Entered text; required digit")
        
user_input=""

while user_input != "exit":
    user_input=input("Enter number of days: ")
    for number in user_input.split(", "):
        # validate_and_execute()
        try_except_validate(number)
    

