def convert_temperature():
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit of temperature (C/F): ")

    if unit.upper() == "C":
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}C is {converted_temp}F")
    elif unit.upper() == "F":
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}F is {converted_temp}C")
    else:
        print("Invalid unit of temperature. Please enter 'C' or 'F'.")

def convert_distance():
    distance = float(input("Enter distance: "))
    unit = input("Enter unit of distance (km/mi): ")

    if unit.lower() == "km":
        converted_distance = distance / 1.609
        print(f"{distance}km is {converted_distance}mi")
    elif unit.lower() == "mi":
        converted_distance = distance * 1.609
        print(f"{distance}mi is {converted_distance}km")
    else:
        print("Invalid unit of distance. Please enter 'km' or 'mi'.")

def main():
    print("Welcome to the temperature/measurement converter app!")
    print("1. Convert temperature (C/F)")
    print("2. Convert distance (km/mi)")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        convert_temperature()
    elif choice == "2":
        convert_distance()
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
