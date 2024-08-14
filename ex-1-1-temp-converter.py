temp_str = input("Enter Celsius temp: ")
celsius = float(temp_str)
fahrenheit = ((9 * celsius) / 5) + 32
# 100, 0, 37,-40
print(f"{celsius:.1f} C is {fahrenheit:.1f} F")