temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
except:
    print("Error --",temp,"is invalid number.")
try:
    cel = (fahr - 32.0) * 5.0 / 9.0
except:
    print("Enter a valid number)
print(cel)
