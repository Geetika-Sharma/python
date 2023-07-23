def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {24 * num_of_days} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {24 * 60 * num_of_days} minutes"

def try_except_validate():
    try:
        input_number = int(days_to_unit_dictionary["days"])
        if input_number > 0:
            print(days_to_units(input_number, days_to_unit_dictionary["unit"]))
        elif input_number == 0:
            print("You entered 0")
        else:
            print("-ve number")
    except ValueError:
        print("Entered text; required digit")
        
user_input=""

while user_input != "exit":
    user_input=input("Enter number of days and unit: ")
    print(user_input)
    if user_input.lower() == "exit":  # Check if user wants to exit
        break
    days_and_unit=user_input.split(":")
    days_to_unit_dictionary={"days": days_and_unit[0], "unit": days_and_unit[1] }
    print(days_and_unit)
    try_except_validate()
