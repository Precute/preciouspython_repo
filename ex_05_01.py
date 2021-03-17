hour_limit = 40
fix_pay = 0
pay = 0
hours = input('Enter the total hours worked: ')
rate = input('Enter your hourly rate: ')

try:
    hours_in_float = float(hours)
    rate_in_float = float(rate)
except:
    print("Error, please enter a numeric input")
    quit()
higher_rate = rate_in_float * 1.5
if  hours_in_float > hour_limit:
    hour_difference = hours_in_float - hour_limit
    addtional_pay = hour_difference * higher_rate
    fix_pay = hour_limit * rate_in_float
    pay = fix_pay + addtional_pay
    print("Includes Overtime")
else:
    print("Regular Pay")
    pay = hours_in_float * rate_in_float
print("Pay: £",pay)
