def calculate_pay(total_hours, payment_rate):
    total = total_hours * payment_rate
    return total

hours = input('Enter the total hours worked: ')
rate = input('Enter your hourly rate: ')
hour_limit = 40
pay = 0
hours_in_float = float(hours)
rate_in_float = float(rate)
higher_rate = rate_in_float * 1.5


if hours_in_float > hour_limit:
    hour_difference = hours_in_float - hour_limit
    pay = calculate_pay(hour_limit,rate_in_float) + calculate_pay(hour_difference, higher_rate)
    print("Overtime")
else:
    print("Regular")
    pay = calculate_pay(hours_in_float,rate_in_float)
print("Pay: £",pay)
