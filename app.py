''' 
    This script converts units of Length, Temperature and Weight.
'''

#Length conversion functions
def convert_to_meters(km):
    return km*1000

def convert_to_kilometers(m):
    return m/1000


# Temperature conversion functions
def convert_to_celsius(f):
    return (f-32)*5/9

def convert_to_fahrenheit(c):
    return 9/5*c+32

# Weight conversion functions
def convert_to_kilograms(g):
    return g/1000

def convert_to_grams(kg):
    return kg*1000



#length conversion menu
def length_menu():
    print("Length Conversion Menu:")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilmeters")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice(1-3): "))
        length = float(input("Enter Length: "))
    except:
        print("Invalid choice. Check for menu options or length inputs.")
        length_menu()
    match choice:
        case 1:
            print(f"{length} kilometers == {convert_to_meters(length)} meters")
            length_menu()
        case 2:
            m = float(input("Enter Length: "))
            print(f"{length} meters == {convert_to_kilometers(length)} kilometers")
            length_menu()
        case 3:
            menu()
        case _:
            print("Invalid choice. Enter 1 - 3 numbers.")
            length_menu()


# Temperature conversion menu
def temperature_menu():
    print("Temperature Conversion Menu:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice(1-3): "))
        temperature = float(input("Enter Temperature: "))
    except:
        print("Invalid choice. Check for menu options or temperature inputs.")
        temperature_menu()
    match choice:
        case 1:
            print(f"{temperature} Fahrenheit == {convert_to_celsius(temperature)} Celsius")
            temperature_menu()
        case 2:
            print(f"{temperature} Celsius == {convert_to_fahrenheit(temperature)} Fahrenheit")
            temperature_menu()
        case 3:
            menu()
        case _:
            print("Invalid choice. Enter 1 - 3 numbers.")
            temperature_menu()


# Weight conversion menu
def weight_menu():
    print("Weight Conversion Menu:")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Grams")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice(1-3): "))
        weight = float(input("Enter Weight: "))
    except:
        print("Invalid choice. Check for menu options or weight inputs.")
        weight_menu()
    match choice:
        case 1:
            print(f"{weight} grams == {convert_to_kilograms(weight)} kilograms")
            weight_menu()
        case 2:
            
            print(f"{weight} kilograms == {convert_to_grams(weight)} grams")
            weight_menu()
        case 3:
            menu()
        case _:
            print("Invalid choice. Enter 1 - 3 numbers.")
            weight_menu()



def menu():
    while True:
        print("Unit Conversion Menu:")
        print("1. Length")
        print("2. Temperature")
        print("3. Weight")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid choice. Enter (1 - 4) numbers.")
            menu()
        match choice:
            case 1:
                length_menu()
            case 2:
                temperature_menu()
            case 3:
                weight_menu()
            case 4:
                exit()
            case _:
                print("Invalid choice. Enter (1 - 4) numbers.")
                menu()


if __name__ == "__main__":
    menu()