def calculate_average(total, times):
    return total/times
total_input = 0.0
number_of_times = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == 'done':
        break
    try:
        float_user_input = float(user_input)
        total_input = total_input + float_user_input
        number_of_times = number_of_times + 1
    except Exception as e:
        print("invalid number")
print("Total:", total_input, ", Average:", calculate_average(total_input,number_of_times))
