# Temperature converter(celcius to fahrenheit)

celcius=float(input("Enter the temp in celcius: "))

f_heit = (celcius*9/5)+32

print("Temp(in Fahrenheit): ",round(f_heit,2))

# Temperature Converter(fahrenheit to celcius)

fah_heit = float(input("\nEnter Temp in fahrenheit: "))

cel = (fah_heit - 32)*5/9

print("Temp(in celcius): ",round(cel,2))