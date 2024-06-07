def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature(value, unit):
    if unit.lower() == 'c':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit.lower() == 'f':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit.lower() == 'k':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        raise ValueError("Invalid unit of measurement. Use 'C', 'F', or 'K'.")

def main():
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ")

        if unit.lower() not in ['c', 'f', 'k']:
            raise ValueError("Invalid unit of measurement. Use 'C', 'F', or 'K'.")

        converted_values = convert_temperature(value, unit)

        if unit.lower() == 'c':
            print(f"{value}°C is equal to {converted_values[0]:.2f}°F and {converted_values[1]:.2f}K")
        elif unit.lower() == 'f':
            print(f"{value}°F is equal to {converted_values[0]:.2f}°C and {converted_values[1]:.2f}K")
        elif unit.lower() == 'k':
            print(f"{value}K is equal to {converted_values[0]:.2f}°C and {converted_values[1]:.2f}°F")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
