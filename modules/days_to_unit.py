from helper import try_except_validate
        
user_input=""

while user_input != "exit":
    user_input=input("Enter number of days and unit: ")
    print(user_input)
    if user_input.lower() == "exit":  # Check if user wants to exit
        break
    days_and_unit=user_input.split(":")
    days_to_unit_dictionary={"days": days_and_unit[0], "unit": days_and_unit[1] }
    print(days_and_unit)
    try_except_validate(days_to_unit_dictionary)
