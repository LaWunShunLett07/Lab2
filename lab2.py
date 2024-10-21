def display_main_menu():
    print("Enter some numbers separated by commas (e.g., 5,67,32)")
    get_user_input = input()
    split_input = get_user_input.split(',')  # Splitting the input by commas
    input_list = [float(item) for item in split_input]  # Convert the strings to floats
    print(input_list)    
    return input_list # Return the list of floats

def calc_average_temperature(input_list):
    total = sum(input_list)  # Summing all elements in the list
    count = len(input_list)  # Get the number of inputs
    average = total / count  # Calculate average
    print("The average temperature is "+str(average))

def calc_min_max_temperature(findmin,findmax):
    minimum=min((findmin))
    maximum=max((findmax))
    inMin=int(minimum)
    inMax=int(maximum)
    print("Minimum is "+str(inMin)+" and Maximum is "+str(inMax))

def sort_temperature():
    input_list.sort()
    print(input_list)

def calc_median_temperature():
    input_list.sort()
    number=len(input_list)
    if number%2 == 0:
        num1=input_list[number//2]
        num2=input_list[number//2-1]
        median=(num1+num2)/2
        print("Even median is "+str(median))
    else:
        median=(input_list[number//2])
        print("Odd median number is "+str(median))


input_list=display_main_menu()
calc_average_temperature(input_list)  
calc_min_max_temperature(input_list,input_list)
sort_temperature()  
calc_median_temperature()