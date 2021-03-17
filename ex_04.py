hours = input('Enter the total hours worked: ')
rate = input('Enter your hourly rate: ')
higher_rate = float(rate) * 1.5
hour_limit = 40
fix_pay = 0
pay = 0
if float(hours) > hour_limit:
    hour_difference = float(hours) - hour_limit
    addtional_pay = hour_difference * higher_rate
    fix_pay = hour_limit * float(rate)
    pay = fix_pay + addtional_pay
    print("Overtime")
else:
    print("Regular")
    pay = float(hours) * float(rate)
print("Pay: £",pay)
