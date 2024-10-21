def display_main_menu():
    print("Enter some numbers separated by commas (e.g., 5,67,32)")
    get_user_input = input()
    split_input = get_user_input.split(',')  # Splitting the input by commas
    input_list = [float(item) for item in split_input]  # Convert the split strings to floats
    print(input_list)
    return input_list  # Return the list of floats

def keep_inputs(num):
    num_of_inputs = len(num)
    return num_of_inputs

def calc_average_temperature(input_list):
    total = sum(input_list)  # Summing all elements in the list
    count = keep_inputs(input_list)  # Get the number of inputs
    average = total / count  # Calculate average
    print(f"The average temperature is: {average}")

def calc_min_max_temperature():
    minimum=min((input_list))
    maximum=max((input_list))
    inMin=int(minimum)
    inMax=int(maximum)
    print("Minimum is "+str(inMin)+" and Maximum is "+str(inMax))

input_list = display_main_menu()
calc_average_temperature(input_list)  
calc_min_max_temperature()