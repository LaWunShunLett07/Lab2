def display_main_menu():
    print("Enter some numbers separated by commas (e.g., 5,67,32)")
    get_user_input = input()
    split_input = get_user_input.split(',')  # Splitting the input by commas
    input_list = [float(item) for item in split_input]  # Convert the strings to floats
    print(input_list)    
    return input_list  # Return the list of floats

def calc_average_temperature(input_list):
    total = sum(input_list)  # Summing all elements in the list
    count = len(input_list)  # Get the number of inputs
    average = total / count  # Calculate average
    print("The average temperature is " + str(average))
    return average

def calc_min_max_temperature(findmin, findmax):
    minimum = min(findmin)
    maximum = max(findmax)
    inMin = int(minimum)
    inMax = int(maximum)
    print("Minimum is " + str(inMin) + " and Maximum is " + str(inMax))
    return inMin, inMax  # Return min and max for testing

def sort_temperature(input_list):
    sorted_list = sorted(input_list)  # Use sorted() to avoid modifying the original list
    print("Sorted list:", sorted_list)
    return sorted_list  # Return sorted list for testing

def calc_median_temperature(input_list):
    sorted_list = sorted(input_list)  # Sort the list
    number = len(sorted_list)
    if number % 2 == 0:
        num1 = sorted_list[number // 2]
        num2 = sorted_list[number // 2 - 1]
        median = (num1 + num2) / 2
        print("Even median is " + str(median))
    else:
        median = sorted_list[number // 2]
        print("Odd median number is " + str(median))
    return median  # Return median for testing

# Function calls for testing purposes
if __name__ == "__main__":
    input_list = display_main_menu()
    calc_average_temperature(input_list)  
    calc_min_max_temperature(input_list, input_list)
    sort_temperature(input_list)  
    calc_median_temperature(input_list)
