import math
def simple_calculator():
    #calculatori
    print()
    print("Hi, welcome to simple calculator, please-read the following instructions.")
    print()
    print("To begin operations - enter anything into the system")
    print()
    print("To add numbers - type + ")
    print("To subtract numbers - type - ")
    print("To multiply numbers - type * ")
    print("To divide numbers - type / ")
    print("To power numbers - type ^")
    print("To get the end result - type = ")
    print()
    print("To end the operations and return, type - stop")
    print("--------------------------------------------------------------------------")

    while True:
        try:
            result = float(input("Please enter the Number: "))
            break
        except:
            print("Invalid number, please try again.")

    while True:

        command = input("Operation: ")
        if command == "return":
            return

        elif command not in ["+", "-", "*", "/", "^", "="]:
            print("Invalid operation")
        elif command == "=":
            print("Final Result:", result)
            break
        elif command == "+":
            while True:
                try:
                    number = float(input("Enter a Number: "))
                    break
                except:
                    print("Invalid number, please try again.")
            result = result + number
            print(result)

        elif command == "-":
            while True:
                try:
                    number = float(input("Enter a Number: "))
                    break
                except:
                    print("Invalid number, please try again.")
            result = result - number
            print(result)
        elif command == "*":
            while True:
                try:
                    number = float(input("Enter a Number: "))
                    break
                except:
                    print("Invalid number, please try again.")
            result = result * number
            print(result)
        elif command == "/":
            while True:
                try:
                    number = float(input("Enter a Number: ")) or number == 0
                    break
                except:
                    print("Invalid number, please try again.")

            result = result / number
            print(result)
        elif command == "^":
            while True:
                try:
                    number = float(input("Enter a Number: "))
                    break
                except:
                    print("Invalid number, please try again.")
            result = result ** number
            print(result)

def unit_converter():
    while True:
        print("Welcome to Unit converter, please follow the following instructions:")
        print()
        print("Please choose the category")
        print("1 - Length")
        print("2 - Temperature")
        print("3 - Mass")
        print("4 - Time")
        print("5 - Area")
        print("6 - Volume")
        print("7 - Speed")
        choice = input("Choice: ")
        if choice == "1":
            length()
        if choice == "2":
            temperature()
        if choice == "3":
            mass()
        if choice == "4":
            time()
        if choice == "5":
            area()
        if choice == "6":
            volume()
        if choice == "7":
            speed()
        elif choice == "return":
            return
        else:
            print("Invalid choice")

def length():
    while True:
        print("Please choose unit you would like to convert from, and the unit you would like to convert to")
        print()
        print("Units included are:")
        print(""
            "1 - Millimeter, "
            "2 - Centimeter, "
            "3 - Decimeter, "
            "4 - Meter, "
            "5 - Kilometer, "
            "6 - Inch, "
            "7 - Foot, "
            "8 - Yard, "
            "9 - Mile")
        From = input("Convert from: ")
        To = input("Convert to: ")
        if From=="return" or To == "return":
            return
        if From == To:
            print("???")
            continue
        while True:
            try:
                value = float(input("Enter value: "))
                break
            except:
                print("Invalid number, try again.")
        if From == "1" and To == "2":
            result = value / 10
            print(result,"Centimeter(s)")
        if From == "1" and To == "3":
            result = value / 100
            print(result,"Decimeter(s)")
        if From == "1" and To == "4":
            result = value / 1000
            print(result,"Meter(s)")
        if From == "1" and To == "5":
            result = value / 1000000
            print(result,"Kilometer(s)")
        if From == "1" and To == "6":
            result = value / 25.4
            print(result,"Inch(s)")
        if From == "1" and To == "7":
            result = value / 304.8
            print(result,"Foot(s)")
        if From == "1" and To == "8":
            result = value / 914.8
            print(result,"Yard(s)")
        if From == "1" and To == "9":
            result = value / 1609344
            print(result,"Mile(s)")

        if From == "2" and To == "1":
            result = value * 10
            print(result, "Millimeters(s)")
        if From == "2" and To == "3":
            result = value / 10
            print(result, "Decimeter(s)")
        if From == "2" and To == "4":
            result = value / 100
            print(result, "Meter(s)")
        if From == "2" and To == "5":
            result = value / 100000
            print(result, "Kilometer(s)")
        if From == "2" and To == "6":
            result = value / 2.54
            print(result, "Inch(s)")
        if From == "2" and To == "7":
            result = value / 30.48
            print(result, "Foot(s)")
        if From == "2" and To == "8":
            result = value / 91.48
            print(result, "Yard(s)")
        if From == "2" and To == "9":
            result = value / 160934.4
            print(result, "Mile(s)")

        if From == "3" and To == "1":
            result = value * 100
            print(result, "Millimeters(s)")
        if From == "3" and To == "2":
            result = value * 10
            print(result, "Centimeter(s)")
        if From == "3" and To == "4":
            result = value / 10
            print(result, "Meter(s)")
        if From == "3" and To == "5":
            result = value / 10000
            print(result, "Kilometer(s)")
        if From == "3" and To == "6":
            result = value / 0.254
            print(result, "Inch(s)")
        if From == "3" and To == "7":
            result = value / 3.048
            print(result, "Foot(s)")
        if From == "3" and To == "8":
            result = value / 9.148
            print(result, "Yard(s)")
        if From == "3" and To == "9":
            result = value / 16093.44
            print(result, "Mile(s)")

        if From == "3" and To == "1":
            result = value * 100
            print(result, "Millimeters(s)")
        if From == "3" and To == "2":
            result = value * 10
            print(result, "Centimeter(s)")
        if From == "3" and To == "4":
            result = value / 10
            print(result, "Meter(s)")
        if From == "3" and To == "5":
            result = value / 10000
            print(result, "Kilometer(s)")
        if From == "3" and To == "6":
            result = value / 0.254
            print(result, "Inch(s)")
        if From == "3" and To == "7":
            result = value / 3.048
            print(result, "Foot(s)")
        if From == "3" and To == "8":
            result = value / 9.148
            print(result, "Yard(s)")
        if From == "3" and To == "9":
            result = value / 16093.44
            print(result, "Mile(s)")

        if From == "4" and To == "1":
            result = value * 1000
            print(result, "Millimeters(s)")
        if From == "4" and To == "2":
            result = value * 100
            print(result, "Centimeter(s)")
        if From == "4" and To == "3":
            result = value * 10
            print(result, "Decimeter(s)")
        if From == "4" and To == "5":
            result = value / 1000
            print(result, "Kilometer(s)")
        if From == "4" and To == "6":
            result = value / 0.0254
            print(result, "Inch(s)")
        if From == "4" and To == "7":
            result = value / 0.3048
            print(result, "Foot(s)")
        if From == "4" and To == "8":
            result = value / 0.9148
            print(result, "Yard(s)")
        if From == "4" and To == "9":
            result = value / 1609.344
            print(result, "Mile(s)")

        if From == "4" and To == "1":
            result = value * 1000
            print(result, "Millimeters(s)")
        if From == "4" and To == "2":
            result = value * 100
            print(result, "Centimeter(s)")
        if From == "4" and To == "3":
            result = value * 10
            print(result, "Decimeter(s)")
        if From == "4" and To == "5":
            result = value / 1000
            print(result, "Kilometer(s)")
        if From == "4" and To == "6":
            result = value / 0.0254
            print(result, "Inch(s)")
        if From == "4" and To == "7":
            result = value / 0.3048
            print(result, "Foot(s)")
        if From == "4" and To == "8":
            result = value / 0.9148
            print(result, "Yard(s)")
        if From == "4" and To == "9":
            result = value / 1609.344
            print(result, "Mile(s)")

        if From == "5" and To == "1":
            result = value * 1000000
            print(result, "Millimeters(s)")
        if From == "5" and To == "2":
            result = value * 100000
            print(result, "Centimeter(s)")
        if From == "5" and To == "3":
            result = value * 10000
            print(result, "Decimeter(s)")
        if From == "5" and To == "4":
            result = value * 1000
            print(result, "Meter(s)")
        if From == "5" and To == "6":
            result = value * 39470.0787
            print(result, "Inch(s)")
        if From == "5" and To == "7":
            result = value * 3280.8399
            print(result, "Foot(s)")
        if From == "5" and To == "8":
            result = value * 1093.6133
            print(result, "Yard(s)")
        if From == "5" and To == "9":
            result = value / 1.609344
            print(result, "Mile(s)")

        if From == "6" and To == "1":
            result = value * 25.4
            print(result, "Millimeter(s)")
        if From == "6" and To == "2":
            result = value * 2.54
            print(result, "Centimeter(s)")
        if From == "6" and To == "3":
            result = value / 3.937
            print(result, "Decimeter(s)")
        if From == "6" and To == "4":
            result = value * 0.0254
            print(result, "Meter(s)")
        if From == "6" and To == "5":
            result = value * 0.0000254
            print(result, "Kilometer(s)")
        if From == "6" and To == "7":
            result = value / 12
            print(result, "Foot(s)")
        if From == "6" and To == "8":
            result = value / 36
            print(result, "Yard(s)")
        if From == "6" and To == "9":
            result = value / 63360
            print(result, "Mile(s)")

        if From == "7" and To == "1":
            result = value * 304.8
            print(result, "Millimeter(s)")
        if From == "7" and To == "2":
            result = value * 30.48
            print(result, "Centimeter(s)")
        if From == "7" and To == "3":
            result = value * 3.048
            print(result, "Decimeter(s)")
        if From == "7" and To == "4":
            result = value * 0.3048
            print(result, "Meter(s)")
        if From == "7" and To == "5":
            result = value / 3280.84
            print(result, "Kilometer(s)")
        if From == "7" and To == "6":
            result = value * 12
            print(result, "Inch(es)")
        if From == "7" and To == "8":
            result = value / 3
            print(result, "Yard(s)")
        if From == "7" and To == "9":
            result = value / 5280
            print(result, "Mile(s)")

        if From == "8" and To == "1":
            result = value * 914.4
            print(result, "Millimeter(s)")
        if From == "8" and To == "2":
            result = value * 91.44
            print(result, "Centimeter(s)")
        if From == "8" and To == "3":
            result = value * 9.144
            print(result, "Decimeter(s)")
        if From == "8" and To == "4":
            result = value * 0.9144
            print(result, "Meter(s)")
        if From == "8" and To == "5":
            result = value / 1093.61
            print(result, "Kilometer(s)")
        if From == "8" and To == "6":
            result = value * 36
            print(result, "Inch(es)")
        if From == "8" and To == "7":
            result = value * 3
            print(result, "Foot(s)")
        if From == "8" and To == "9":
            result = value / 1760
            print(result, "Mile(s)")

        if From == "9" and To == "1":
            result = value * 1609344
            print(result, "Millimeter(s)")
        if From == "9" and To == "2":
            result = value * 160934.4
            print(result, "Centimeter(s)")
        if From == "9" and To == "3":
            result = value * 16093.44
            print(result, "Decimeter(s)")
        if From == "9" and To == "4":
            result = value * 1609.344
            print(result, "Meter(s)")
        if From == "9" and To == "5":
            result = value * 1.609344
            print(result, "Kilometer(s)")
        if From == "9" and To == "6":
            result = value * 63360
            print(result, "Inch(es)")
        if From == "9" and To == "7":
            result = value * 5280
            print(result, "Foot(s)")
        if From == "9" and To == "8":
            result = value * 1760
            print(result, "Yard(s)")

        again = input("Convert another value? (yes/no): ")
        if again == "yes":
            continue
        else:
            return

def temperature():
    while True:
        print("Please choose unit you would like to convert from, and the unit you would like to convert to")
        print()
        print("Units included are:")
        print(""
            "1 - Celsius(°C),"
            "2 - Fahrenheit(°F),"
            "3 - Kelvin(K),"
            )
        From = input("Convert from: ")
        To = input("Convert to: ")
        if From =="return" or To == "return":
            return
        if From == To:
            print("???")
            continue
        while True:
            try:
                value = float(input("Enter value: "))
                break
            except:
                print("Invalid number, try again.")
        if From == "1" and value < -273.15:
            print("Invalid temperature. Celsius cannot be below -273.15°C.")
            continue
        if From == "2" and value < -459.67:
            print("Invalid temperature. Fahrenheit cannot be below -459.67°F.")
            continue
        if From == "3" and value < 0:
            print("Invalid temperature. Kelvin cannot be below 0 K.")
            continue

        if From == "1" and To == "2":
            result = (value * 9 / 5) + 32
            print(result, "°F")
        if From == "1" and To == "3":
            result = value + 273.15
            print(result, "K")

        if From == "2" and To == "1":
            result = (value - 32) * 5 / 9
            print(result, "°C")
        if From == "2" and To == "3":
            result = (value - 32) * 5 / 9 + 273.15
            print(result, "K")

        if From == "3" and To == "1":
            result = value - 273.15
            print(result, "°C")
        if From == "3" and To == "2":
            result = (value - 273.15) * 9 / 5 + 32
            print(result, "°F")

        again = input("Convert another value? (yes/no): ")
        if again == "yes":
            continue
        else:
            return

def mass():
    while True:
        print("Please choose unit you would like to convert from, and the unit you would like to convert to")
        print()
        print("Units included are:")
        print(""
            "1 - Milligram(s) - (Mg),"
            "2 - Grams(s) - (g),"
            "3 - Kilogram(s) - (Kg),"
            "4 - Pounds(s) - (lb)"
            "5 - Ounce(s) - (oz)"
            )
        From = input("Convert from: ")
        To = input("Convert to: ")
        if From == "return" or To == "return":
            return
        if From == To:
            print("???")
            continue
        while True:
            try:
                value = float(input("Enter value: "))
                break
            except:
                print("Invalid number, try again.")

        if From == {"1", "2", "3", "4", "5"} and value < 0:
            print("Not sure if that's possible")
            continue

        if From == "1" and To == "2":
            result = value / 1000
            print(result, "Gram(s)")
        if From == "1" and To == "3":
            result = value / 1000000
            print(result, "Kilogram(s)")
        if From == "1" and To == "4":
            result = value / 453592.37
            print(result, "Pound(s)")
        if From == "1" and To == "5":
            result = value / 28349.523125
            print(result, "Ounce(s)")

        if From == "2" and To == "1":
            result = value * 1000
            print(result, "Milligram(s)")
        if From == "2" and To == "3":
            result = value / 1000
            print(result, "Kilogram(s)")
        if From == "2" and To == "4":
            result = value / 453.59237
            print(result, "Pound(s)")
        if From == "2" and To == "5":
            result = value / 28.349523125
            print(result, "Ounce(s)")

        if From == "3" and To == "1":
            result = value * 1000000
            print(result, "Milligram(s)")
        if From == "3" and To == "2":
            result = value * 1000
            print(result, "Gram(s)")
        if From == "3" and To == "4":
            result = value * 2.20462262
            print(result, "Pound(s)")
        if From == "3" and To == "5":
            result = value * 35.2739619
            print(result, "Ounce(s)")

        if From == "4" and To == "1":
            result = value * 453592.37
            print(result, "Milligram(s)")
        if From == "4" and To == "2":
            result = value * 453.59237
            print(result, "Gram(s)")
        if From == "4" and To == "3":
            result = value / 2.20462262
            print(result, "Kilogram(s)")
        if From == "4" and To == "5":
            result = value * 16
            print(result, "Ounce(s)")

        if From == "5" and To == "1":
            result = value * 28349.523125
            print(result, "Milligram(s)")
        if From == "5" and To == "2":
            result = value * 28.349523125
            print(result, "Gram(s)")
        if From == "5" and To == "3":
            result = value / 35.2739619
            print(result, "Kilogram(s)")
        if From == "5" and To == "4":
            result = value / 16
            print(result, "Pound(s)")
        again = input("Convert another value? (yes/no): ")
        if again == "yes":
            continue
        else:
            return


def time():
    while True:
        print("Please choose unit you would like to convert from, and the unit you would like to convert to")
        print()
        print("Units included are:")
        print(
            "1 - Second(s) - (s), "
            "2 - Minute(s) - (min), "
            "3 - Hour(s) - (hr), "
            "4 - Day(s) - (day), "
            "5 - Week(s) - (week), "
            "6 - Year(s) - (yr)"
        )
        From = input("Convert from: ")
        To = input("Convert to: ")
        if From == "return" or To == "return":
            return
        if From == To:
            print("???")
            continue
        while True:
            try:
                value = float(input("Enter value: "))
                break
            except:
                print("Invalid number, try again.")
        if value < 0:
            print("Not sure if that's possible.")
            continue
        again = input("Convert another value? (yes/no): ")
        if again == "yes":
            continue
        else:
            return

    if From == "1" and To == "2":
        result = value / 60
        print(result, "Minute(s)")
    if From == "1" and To == "3":
        result = value / 3600
        print(result, "Hour(s)")
    if From == "1" and To == "4":
        result = value / 86400
        print(result, "Day(s)")
    if From == "1" and To == "5":
        result = value / 604800
        print(result, "Week(s)")
    if From == "1" and To == "6":
        result = value / 31536000
        print(result, "Year(s)")

    if From == "2" and To == "1":
        result = value * 60
        print(result, "Second(s)")
    if From == "2" and To == "3":
        result = value / 60
        print(result, "Hour(s)")
    if From == "2" and To == "4":
        result = value / 1440
        print(result, "Day(s)")
    if From == "2" and To == "5":
        result = value / 10080
        print(result, "Week(s)")
    if From == "2" and To == "6":
        result = value / 525600
        print(result, "Year(s)")

    if From == "3" and To == "1":
        result = value * 3600
        print(result, "Second(s)")
    if From == "3" and To == "2":
        result = value * 60
        print(result, "Minute(s)")
    if From == "3" and To == "4":
        result = value / 24
        print(result, "Day(s)")
    if From == "3" and To == "5":
        result = value / 168
        print(result, "Week(s)")
    if From == "3" and To == "6":
        result = value / 8760
        print(result, "Year(s)")

    if From == "4" and To == "1":
        result = value * 86400
        print(result, "Second(s)")
    if From == "4" and To == "2":
        result = value * 1440
        print(result, "Minute(s)")
    if From == "4" and To == "3":
        result = value * 24
        print(result, "Hour(s)")
    if From == "4" and To == "5":
        result = value / 7
        print(result, "Week(s)")
    if From == "4" and To == "6":
        result = value / 365
        print(result, "Year(s)")

    if From == "5" and To == "1":
        result = value * 604800
        print(result, "Second(s)")
    if From == "5" and To == "2":
        result = value * 10080
        print(result, "Minute(s)")
    if From == "5" and To == "3":
        result = value * 168
        print(result, "Hour(s)")
    if From == "5" and To == "4":
        result = value * 7
        print(result, "Day(s)")
    if From == "5" and To == "6":
        result = value / 52.1429
        print(result, "Year(s)")

    if From == "6" and To == "1":
        result = value * 31536000
        print(result, "Second(s)")
    if From == "6" and To == "2":
        result = value * 525600
        print(result, "Minute(s)")
    if From == "6" and To == "3":
        result = value * 8760
        print(result, "Hour(s)")
    if From == "6" and To == "4":
        result = value * 365
        print(result, "Day(s)")
    if From == "6" and To == "5":
        result = value * 52.1429
        print(result, "Week(s)")

def area():
    while True:
        print("Please choose unit you would like to convert from, and the unit you would like to convert to")
        print()
        print("Units included are:")
        print(
            "1 - Square Centimeter (cm²), "
            "2 - Square Meter (m²), "
            "3 - Square Kilometer (km²), "
            "4 - Square Foot (ft²), "
            "5 - Acre"
        )
        From = input("Convert from: ")
        To = input("Convert to: ")
        if From == "return" or To == "return":
            return
        if From == To:
            print("???")
            continue
        while True:
            try:
                value = float(input("Enter value: "))
                break
            except:
                print("Invalid number, try again.")
        if value < 0:
            print("Not sure if that's possible.")
            continue
        if From == "1" and To == "2":
            result = value / 10000
            print(result, "Square Meter(s)")
        if From == "1" and To == "3":
            result = value / 10000000000
            print(result, "Square Kilometer(s)")
        if From == "1" and To == "4":
            result = value / 929.0304
            print(result, "Square Foot(s)")
        if From == "1" and To == "5":
            result = value / 40468564.224
            print(result, "Acre(s)")

        if From == "2" and To == "1":
            result = value * 10000
            print(result, "Square Centimeter(s)")
        if From == "2" and To == "3":
            result = value / 1000000
            print(result, "Square Kilometer(s)")
        if From == "2" and To == "4":
            result = value * 10.7639104
            print(result, "Square Foot(s)")
        if From == "2" and To == "5":
            result = value / 4046.8564224
            print(result, "Acre(s)")


        if From == "3" and To == "1":
            result = value * 10000000000
            print(result, "Square Centimeter(s)")
        if From == "3" and To == "2":
            result = value * 1000000
            print(result, "Square Meter(s)")
        if From == "3" and To == "4":
            result = value * 10763910.4
            print(result, "Square Foot(s)")
        if From == "3" and To == "5":
            result = value * 247.105381
            print(result, "Acre(s)")

        if From == "4" and To == "1":
            result = value * 929.0304
            print(result, "Square Centimeter(s)")
        if From == "4" and To == "2":
            result = value / 10.7639104
            print(result, "Square Meter(s)")
        if From == "4" and To == "3":
            result = value / 10763910.4
            print(result, "Square Kilometer(s)")
        if From == "4" and To == "5":
            result = value / 43560
            print(result, "Acre(s)")

        if From == "5" and To == "1":
            result = value * 40468564.224
            print(result, "Square Centimeter(s)")
        if From == "5" and To == "2":
            result = value * 4046.8564224
            print(result, "Square Meter(s)")
        if From == "5" and To == "3":
            result = value / 247.105381
            print(result, "Square Kilometer(s)")
        if From == "5" and To == "4":
            result = value * 43560
            print(result, "Square Foot(s)")

        again = input("Convert another value? (yes/no): ")
        if again == "yes":
            continue
        else:
            return

def volume():
    while True:
        print("Please choose unit you would like to convert from, and the unit you would like to convert to")
        print()
        print("Units included are:")
        print(
            "1 - Milliliter (mL), "
            "2 - Liter (L), "
            "3 - Cubic Centimeter (cm³), "
            "4 - Cubic Meter (m³), "
            "5 - Gallon (gal), "
            "6 - Cubic Foot (ft³)"
        )

        From = input("Convert from: ")
        To = input("Convert to: ")
        if From == "return" or To == "return":
            return
        if From == To:
            print("???")
            continue
        while True:
            try:
                value = float(input("Enter value: "))
                break
            except:
                print("Invalid number, try again.")
        if value < 0:
            print("Not sure if that's possible.")
            continue
        if From == "1" and To == "2":
            result = value / 1000
            print(result, "Liter(s)")
        if From == "1" and To == "3":
            result = value
            print(result, "Cubic Centimeter(s)")
        if From == "1" and To == "4":
            result = value / 1000000
            print(result, "Cubic Meter(s)")
        if From == "1" and To == "5":
            result = value / 3785.411784
            print(result, "Gallon(s)")
        if From == "1" and To == "6":
            result = value / 28316.846592
            print(result, "Cubic Foot(s)")

        if From == "2" and To == "1":
            result = value * 1000
            print(result, "Milliliter(s)")
        if From == "2" and To == "3":
            result = value * 1000
            print(result, "Cubic Centimeter(s)")
        if From == "2" and To == "4":
            result = value / 1000
            print(result, "Cubic Meter(s)")
        if From == "2" and To == "5":
            result = value / 3.785411784
            print(result, "Gallon(s)")
        if From == "2" and To == "6":
            result = value / 28.316846592
            print(result, "Cubic Foot(s)")

        if From == "3" and To == "1":
            result = value
            print(result, "Milliliter(s)")
        if From == "3" and To == "2":
            result = value / 1000
            print(result, "Liter(s)")
        if From == "3" and To == "4":
            result = value / 1000000
            print(result, "Cubic Meter(s)")
        if From == "3" and To == "5":
            result = value / 3785.411784
            print(result, "Gallon(s)")
        if From == "3" and To == "6":
            result = value / 28316.846592
            print(result, "Cubic Foot(s)")

        if From == "4" and To == "1":
            result = value * 1000000
            print(result, "Milliliter(s)")
        if From == "4" and To == "2":
            result = value * 1000
            print(result, "Liter(s)")
        if From == "4" and To == "3":
            result = value * 1000000
            print(result, "Cubic Centimeter(s)")
        if From == "4" and To == "5":
            result = value * 264.172052
            print(result, "Gallon(s)")
        if From == "4" and To == "6":
            result = value * 35.3146667
            print(result, "Cubic Foot(s)")

        if From == "5" and To == "1":
            result = value * 3785.411784
            print(result, "Milliliter(s)")
        if From == "5" and To == "2":
            result = value * 3.785411784
            print(result, "Liter(s)")
        if From == "5" and To == "3":
            result = value * 3785.411784
            print(result, "Cubic Centimeter(s)")
        if From == "5" and To == "4":
            result = value / 264.172052
            print(result, "Cubic Meter(s)")
        if From == "5" and To == "6":
            result = value / 7.48051948
            print(result, "Cubic Foot(s)")

        if From == "6" and To == "1":
            result = value * 28316.846592
            print(result, "Milliliter(s)")
        if From == "6" and To == "2":
            result = value * 28.316846592
            print(result, "Liter(s)")
        if From == "6" and To == "3":
            result = value * 28316.846592
            print(result, "Cubic Centimeter(s)")
        if From == "6" and To == "4":
            result = value / 35.3146667
            print(result, "Cubic Meter(s)")
        if From == "6" and To == "5":
            result = value * 7.48051948
            print(result, "Gallon(s)")

        again = input("Convert another value? (yes/no): ")
        if again == "yes":
            continue
        else:
            return

def speed():
    while True:
        print("Please choose unit you would like to convert from, and the unit you would like to convert to")
        print()
        print("Units included are:")
        print(
            "1 - Meter per Second (m/s), "
            "2 - Kilometer per Hour (km/h), "
            "3 - Foot per Second (ft/s), "
            "4 - Mile per Hour (mph)"
        )
        From = input("Convert from: ")
        To = input("Convert to: ")
        if From == "return" or To == "return":
            return
        if From == To:
            print("???")
            continue
        while True:
            try:
                value = float(input("Enter value: "))
                break
            except:
                print("Invalid number, try again.")
        if value < 0:
            print("Not sure if that's possible.")
            continue
        if From == "1" and To == "2":
            result = value * 3.6
            print(result, "km/h")
        if From == "1" and To == "3":
            result = value * 3.2808399
            print(result, "ft/s")
        if From == "1" and To == "4":
            result = value * 2.23693629
            print(result, "mph")
        if From == "2" and To == "1":
            result = value / 3.6
            print(result, "m/s")
        if From == "2" and To == "3":
            result = value / 1.09728
            print(result, "ft/s")
        if From == "2" and To == "4":
            result = value / 1.609344
            print(result, "mph")
        if From == "3" and To == "1":
            result = value / 3.2808399
            print(result, "m/s")
        if From == "3" and To == "2":
            result = value * 1.09728
            print(result, "km/h")
        if From == "3" and To == "4":
            result = value / 1.46666667
            print(result, "mph")
        if From == "4" and To == "1":
            result = value / 2.23693629
            print(result, "m/s")
        if From == "4" and To == "2":
            result = value * 1.609344
            print(result, "km/h")
        if From == "4" and To == "3":
            result = value * 1.46666667
            print(result, "ft/s")
        again = input("Convert another value? (yes/no): ")
        if again == "yes":
            continue
        else:
            return


def geometric_calculator():
    while True:
        print("Welcome to Geomtric calculator. Please follow the following instructions")
        print("Please choose the dimension of the figure")
        print()
        print("1 - 2D shape")
        print("2 - 3D shape")
        print("3 - to return")
        while True:
            try:
                value = float(input("Please pick the shape(1 - 2D or 2 - 3D or 3(to return)): "))
                if value == 3:
                    return
                elif value == 1:
                    print("you chose 2D figure")
                    shape()
                elif value == 2:
                    print("you chose 3D shape")
                    shapee()
                else:
                    print("Please enter either 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
def shape():
    while True:
        try:
            sides = int(input("Enter the number of sides (0 for a circle(Elipses, hyperbolas, parabolas not included)): "))

            if sides == 0:
                print("You selected a circle.")
                print("\nWhat'd you like to calculate?")
                print("1 - Circumference")
                print("2 - Area")
                choice = int(input("Choice: "))
                if choice == 1:
                    print("Circumference will be calculated.")
                    break
                elif choice == 2:
                    print("Area will be calculated.")
                    break
                else:
                    print("Please enter 1 or 2.")
            elif sides >= 3:
                print(f"You selected a {sides}-sided polygon.")
                while True:
                    try:
                        print("\nIs the polygon regular?")
                        print("1 - Yes")
                        print("2 - No")
                        regularity = int(input("Choice: "))
                        if regularity == 1:
                            print("Regular polygon selected.")
                            print("\nWhat'd you like to calculate?")
                            print("1 - Perimeter")
                            print("2 - Area")
                            choice = int(input("Choice: "))
                            regular_shape_calc_2d(sides, choice)
                            return
                        elif regularity == 2:
                            print("Irregular polygon selected.")
                            print("\nWhat'd you like to calculate?")
                            print("1 - Perimeter")
                            print("2 - Area")
                            choice = int(input("Choice: "))
                            irregular_shape_calc_2d(sides, choice)
                            return
                        else:
                            print("Please enter 1 or 2.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                print("A polygon must have at least 3 sides.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def regular_shape_calc_2d(sides, choice):
    if sides == 0:
        print("Please enter the Radius")
        radius = float(input("Radius = "))
        if choice == 2:
            area = math.pi * radius**2
            print(f"Area of the circle = {area}")
        elif choice == 1:
            circumference = 2 * math.pi * radius
            print(f"Circumference of the circle = {circumference}")
    elif sides >= 3:
        print("Please enter length of the side")
        length = float(input("Length = "))
        if choice == 1:
            perimeter = sides * length
            print(f"Perimeter of the polygon = {perimeter}")
        elif choice == 2:
            area = (length**2) * sides / (4 * math.tan(math.pi / sides))
            print(f"Area of the polygon = {area}")

def irregular_shape_calc_2d(sides, choice):
    if sides == 3 and choice == 1:
        print("Please enter the sides of the figure")
        a = float(input("first side of the figure = "))
        b = float(input("second side of the figure = "))
        c = float(input("third side of the figure = "))
        if a+b<=c:
            print("Invalid, Triangle doesn't exist")
        elif a+c<=b:
            print("Invalid, Triangle doesn't exist")
        elif c+b<=a:
            print("Invalid, Triangle doesn't exist")
        else:
            perimeter = (a + b + c)
            print(f"Perimeter of the triangle = {perimeter}")
    elif sides == 3 and choice == 2:
        print("Please answer the following questions")
        print("do you know all 3 sides of the triangle?")
        print("1 - Yes")
        print("2 - No")
        value = int(input("Choice: "))
        if value == 1:
            print("Please enter the said sides.")
            a = float(input("First side of the triangle = "))
            b = float(input("Second side of the triangle = "))
            c = float(input("Third side of the triangle = "))
            if a+b <= c or a+c<=b or b+c<=a or a<=0 or b<=0 or c<=0:
                print("Invalid input")
            else:
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                print(f"Area of the triangle = {area}")
        if value == 2:
            print("Please answer the following questions")
            print("do you know two neighbouring sides and the angle between them?")
            print("1 - Yes")
            print("2 - No")
            value = int(input("Choice: "))
            if value == 1:
                print("Please enter the said sides and the angle between them.")
                a = float(input("First side of the triangle = "))
                b = float(input("Second side of the triangle = "))
                alpha = float(input("Enter the angle (in degrees): "))
                alpha = math.radians(alpha)
                area = 0.5*a*b*math.sin(alpha)
                print(f"Area of the triangle = {area}")
            if value == 2:
                print("Please answer the following questions")
                print("Do you know one side of a triangle and the height of that side relative to the opposite angle?")
                print("1 - Yes")
                print("2 - No")
                value = int(input("Choice: "))
                if value == 1:
                    print("Please enter the said side and the height of the triangle")
                    a = float(input(" side of the triangle = "))
                    h = float(input("height of the triangle = "))
                    if a or h <0:
                        print("Invalid input")
                    else:
                        area = 0.5* a*h
                        print(f"Area of the triangle = {area}")
                if value == 2:
                    print("Not enough information.")

    if sides == 4 and choice == 1:
        print("Please enter sides of the figure")
        a = float(input("First side of the figure = "))
        b = float(input("Second side of the figure = "))
        c = float(input("Third side of the figure = "))
        d = float(input("Fourth side of the figure = "))
        if a<0 or b<0 or c<0 or d <0:
            print("Invalid input")
        else:
            perimeter = (a + b + c + d)
            print(f"Perimeter of the polygon = {perimeter}")
    elif sides == 4 and choice == 2:
        print("Are opposite pairs of the quadrilateral parallel to eachother?")
        print("1 - Yes")
        print("2 - No")
        value = int(input("Choice: "))
        if value == 1:
            print("do you know two neighbouring sides and the angle between them?")
            print("1 - Yes")
            print("2 - No")
            value = int(input("Choice: "))
            if value == 1:
                print("Please enter the said sides and the angle between them.")
                a = float(input("First side of the figure = "))
                b = float(input("Second side of the figure = "))
                alpha = float(input("Enter the angle (in degrees): "))
                if a < 0 or b<0 or math.sin(alpha) <0:
                    print("Invalid input")
                else:
                    area = a*b*math.sin(alpha)
                    print(f"Area of the quadrilateral (Parallelogram) = {area}")
            elif value == 2:
                print("do you know one side and the height from the opposite angle?")
                print("1 - Yes")
                print("2 - No")
                value = int(input("Choice: "))
                if value == 1:
                    print("Please enter the said side and the height from the opposite angle")
                    a = float(input("side of the figure = "))
                    h = float(input("height from the opposite angle = "))
                    area = a*h
                    print(f"Area of the quadrilateral (Parallelogram) = {area}")
                elif value == 2:
                    print("Not enough information.")
        elif value == 2:
            print("are 2 sides parallel to eachother?")
            print("1 - Yes")
            print("2 - No")
            value = int(input("Choice: "))
            if value == 2:
                print("not enough information.")
            elif value == 1:
                print("Please enter the said sides and the height/distance between them")
                a = float(input("one side of the figure = "))
                b = float(input("second sides of the figure = "))
                h = float(input("distance between them = "))
                if a<0 or b<0 or h < 0:
                    print("Can't have a negative length. Invalid")
                else:
                    area = h*0.5*(a+b)
                    print(f"Area of the quadrilateral (Trapezoid) = {area}")


            else:
                print("pls enter either 1 or 2")



def shapee():
    print("Please choose solid type")
    print("1 - Prism")
    print("2 - Pyramid")
    print("3 - Cylinder")
    print("4 - Sphere")
    print("5 - Cone")
    type = int(input("Choice: "))
    if type == 1:
        print()
        print("Please choose the shape of the base")
        print("1 - Triangle")
        print("2 - Trapezoid")
        print("3 - Parallelogram")
        print("4 - Regular Polygon")
        base = int(input("Choice: "))
        if base == 1:
            prism_triangle_3d()
        elif base == 2 or base == 3 or base == 4:
            different_figure_3d()
        else:
            print("Invalid input")
    elif type == 2:
        pyramid_3d()
    elif type == 4:
        sphere_3d()
    elif type == 3:
        cylinder_3d()
    elif type == 5:
        cone_3d()
    else:
        print("Invalid input")

def prism_triangle_3d():
    print("Is the triangle regular?")
    print("1 - Yes")
    print("2 - No")
    answer = int(input("Choice: "))
    print()
    print("Please choose the question")
    print("1 - Surface Area of the figure")
    print("2 - Volume of the figure")
    q_1 = int(input("Choice: "))
    if answer == 1 and q_1 == 2:
        print("Please enter the side of the base/triangle")
        a = float(input("side of the base = "))
        print("Please enter the height of the solid")
        h = float(input("height of the solid = "))
        s_a = (a**2)*(3**0.5)*0.25
        vol = s_a*h
        print(f"Volume of the figure = {vol}")
    elif answer == 1 and q_1 == 1:
        print("Please enter the side of the base/triangle")
        a = float(input("side of the base = "))
        s_a = (a**2)*(3**0.5)*0.25
        print("Please enter the height of the solid")
        h = float(input("solid's lateral face's side = "))
        alpha = float(input("Enter the angle (in degrees) of solid's lateral face: "))
        alpha = math.radians(alpha)
        lat_s = a * h * math.sin(alpha)
        sf_a = 3*lat_s + 2*s_a
        print(f"Surface Area of the Prism = {sf_a}")
    elif answer == 2 and q_1 == 1:
        print("Please enter the Area of the triangle (You can use our 2D calculator for that <3")
        s = float(input("Area of the triangle = "))
        print("Please enter the height of the solid")
        h = float(input("height of the solid = "))
        vol = s * h
        print(f"Volume of the Prism = {vol}")
    elif answer == 2 and q_1 == 2:
        print("Please enter the Area of the triangle (You can use our 2D calculator for that <3")
        a = float(input("Area of the triangle = "))
        print("Please enter the sides of the solid")
        b = float(input("sides of the solid = "))
        area = 4*b + 2*a
        print(f"Surface area of the Prism = {area}")
    else:
        print("Invalid input")


def different_figure_3d():
    print("Please choose the question")
    print("1 - Surface Area of the figure")
    print("2 - Volume of the figure")
    q_1 = int(input("Choice: "))
    if q_1 == 1:
        print("Please enter the base area of the figure (for that you can use our 2D calculator for that <3")
        a = float(input("base area of the figure = "))
        print("Please enter the lateral side's area of the figure (for that you can use our 2D calculator for that <3)")
        b = float(input("lateral side's area of the figure = "))
        s_a = 2*a + 4*b
        print(f"Surface Area of the Prism = {s_a}")
    elif q_1 == 2:
        print("Please enter the base area of the figure (for that you can use our 2D calculator for that <3)")
        a = float(input("base area of the figure = "))
        print("Please enter the height of the figure")
        h = float(input("height of the figure = "))
        vol = a * h
        print(f"Volume of the Prism = {vol}")
    else:
        print("Invalid input")


def pyramid_3d():
    print("Please enter what you'd like to calculate")
    print("1 - Surface Area")
    print("2 - Volume")
    q_1 = int(input("Choice: "))
    if q_1 == 1:
        print("please enter base length")
        l = float(input("base length = "))
        print("Please enter the base width")
        w = float(input("base width = "))
        print("Please enter the pyramid height")
        h = float(input("pyramid height = "))
        s_a = l*w + l*((((w*1/2)**2)+(h**2))**(1/2)) + w * (((l/2)**2)+ (h**2))**(1/2)
        print(f"Surface Area of the Prism = {s_a}")
    elif q_1 == 2:
        print("please enter the base area")
        s = float(input("base area = "))
        print("Please enter the height of the figure")
        h = float(input("height of the figure = "))
        vol = s * h * (1/3)
        print(f"Volume of the Prism = {vol}")
    else:
        print("Invalid input")

def sphere_3d():
    print("Please enter what you'd like to calculate")
    print("1 - Surface Area")
    print("2 - Volume")
    q_1 = int(input("Choice: "))
    if q_1 == 1:
        print("please radius")
        r = float(input("radius = "))
        s_a = (r**2)* math.pi * 4
        print(f"Surface Area of the Sphere = {s_a}")
    elif q_1 == 2:
        print("please enter the radius")
        s = float(input("radius = "))
        vol = 4/3 * math.pi * (s**3)
        print(f"Volume of the Prism = {vol}")
    else:
        print("Invalid input")

def cylinder_3d():
    print("Please enter what you'd like to calculate")
    print("1 - Surface Area")
    print("2 - Volume")
    q_1 = int(input("Choice: "))
    if q_1 == 2:
        print("Please enter base area(Can be found by using our 2D calculator for that <3")
        a = float(input("base area = "))
        print("Please enter the height of the sphere")
        h = float(input("height of the sphere = "))
        vol = a * h
        print(f"Volume of the Prism = {vol}")
    elif q_1 == 1:
        print("Please enter the base area(Can be found by using our 2D calculator for that <3")
        a = float(input("base area = "))
        print("Please enter the height of the sphere")
        h = float(input("height of the sphere = "))
        s_a = 2*h + 2*a
        print(f"Surface Area of the Prism = {s_a}")

def cone_3d():
    print("Please enter what you'd like to calculate")
    print("1 - Surface Area")
    print("2 - Volume")
    q_1 = int(input("Choice: "))
    if q_1 == 1:
        print("Please enter base area(Can be found by using our 2D calculator for that <3")
        s = float(input("base area = "))
        print("Please enter the height of the cone")
        h = float(input("height of the sphere = "))
        vol = s * h * (1/3)
        print(f"Volume of the Prism = {vol}")
    elif q_1 == 2:
        print("please enter radius of the cone")
        r = float(input("radius = "))
        print("Please enter the height of the cone")
        h = float(input("height of the cone = "))
        s_a = math.pi * r * (r+ ((h**2 + (r**2))**(1/2) ))
        print(f"Surface Area of the Prism = {s_a}")
    else:
        print("Invalid input")

import math

def scientific_calculator():
    while True:
        print()
        print("Scientific Calculator")
        print("Please choose an operation")
        print("1 - Power")
        print("2 - Square root")
        print("3 - Cube root")
        print("4 - Sine")
        print("5 - Cosine")
        print("6 - Tangent")
        print("7 - Common logarithm (log base 10)")
        print("8 - Natural logarithm (ln)")
        print("9 - Factorial")
        print("10 - Absolute value")
        print("11 - Degrees to radians")
        print("12 - Radians to degrees")
        print("Type 'return' to return to the previous menu")

        choice = input("Choice: ").strip().lower()

        if choice == "return":
            return

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 12.")
            continue
        if choice == 1:
            try:
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                result = base ** exponent
                print(f"Result = {result}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
            except OverflowError:
                print("The result is too large.")
            except ZeroDivisionError:
                print("Zero cannot be raised to a negative power.")
        elif choice == 2:
            try:
                number = float(input("Enter the number: "))
                if number < 0:
                    print("Cannot calculate the square root of a negative number.")
                else:
                    result = math.sqrt(number)
                    print(f"Square root = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 3:
            try:
                number = float(input("Enter the number: "))
                if number >= 0:
                    result = number ** (1 / 3)
                else:
                    result = -((-number) ** (1 / 3))
                print(f"Cube root = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 4:
            try:
                angle = float(input("Enter the angle in degrees: "))
                angle_radians = math.radians(angle)
                result = math.sin(angle_radians)
                if abs(result) < 1e-12:
                    result = 0.0
                print(f"Sine of {angle} degrees = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid angle.")
        elif choice == 5:
            try:
                angle = float(input("Enter the angle in degrees: "))
                angle_radians = math.radians(angle)
                result = math.cos(angle_radians)
                if abs(result) < 1e-12:
                    result = 0.0
                print(f"Cosine of {angle} degrees = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid angle.")
        elif choice == 6:
            try:
                angle = float(input("Enter the angle in degrees: "))
                angle_radians = math.radians(angle)
                if abs(math.cos(angle_radians)) < 1e-12:
                    print("Tangent is undefined for this angle.")
                else:
                    result = math.tan(angle_radians)
                    if abs(result) < 1e-12:
                        result = 0.0
                    print(f"Tangent of {angle} degrees = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid angle.")
        elif choice == 7:
            try:
                number = float(input("Enter the number: "))
                if number <= 0:
                    print("A logarithm can only be calculated for a positive number.")
                else:
                    result = math.log10(number)
                    print(f"log₁₀({number}) = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 8:
            try:
                number = float(input("Enter the number: "))
                if number <= 0:
                    print("A logarithm can only be calculated for a positive number.")
                else:
                    result = math.log(number)
                    print(f"ln({number}) = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 9:
            try:
                number = input("Enter a non-negative integer: ").strip()
                if "." in number:
                    print("Factorial can only be calculated for whole numbers.")
                    continue
                number = int(number)
                if number < 0:
                    print("Factorial cannot be calculated for a negative number.")
                else:
                    result = math.factorial(number)
                    print(f"{number}! = {result}")
            except ValueError:
                print("Invalid input. Please enter a non-negative integer.")
        elif choice == 10:
            try:
                number = float(input("Enter the number: "))
                result = abs(number)
                print(f"Absolute value = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 11:
            try:
                degrees = float(input("Enter the angle in degrees: "))
                radians = math.radians(degrees)
                print(f"{degrees} degrees = {radians} radians")
            except ValueError:
                print("Invalid input. Please enter a valid angle.")
        elif choice == 12:
            try:
                radians = float(input("Enter the angle in radians: "))
                degrees = math.degrees(radians)
                print(f"{radians} radians = {degrees} degrees")
            except ValueError:
                print("Invalid input. Please enter a valid angle.")
        else:
            print("Invalid choice. Please enter a number from 1 to 12.")

def instructions():
    print("enter which section you want to know about")
    print()
    print("1 - Simple Calculator")
    print("2 - Unit Converter")
    print("3 - Geometry Calculator")
    print("4 - Scientific Calculator (Not to be confused with expressional calculator)")
    print("stop - Exit and go back to calculator suite")
    choice = int(input("Choice: "))
    if choice == 1:
        print("Instructions of the simple calculator")
        print()
        print("Can do Several expressions, including substraction, addition, multiplication, and division.")
        print("However please avoid entering too much of complex and irregular expressions, as it may damage the system or simply lag out the python language.")
        print()
        print("please enter return to return to the main menu, from where you can close the system")
    elif choice == 2:
        print("Instructions of the unit converter")
        print()
        print("Unit converter including time, speed, lengths and others.")
        print("Please avoid entering complex expressions, as once again it may damage the system")
        print("please avoid entering texts in place of numbers and vice versa.")
        print()
        print("Please enter return to return to the main menu, from where you can close the system")
    elif choice == 3:
        print("Instructions of the geometry calculator")
        print()
        print("Please avoid entering texts in place of numbers and vice versa")
        print("2D calculator can calculate area and perimeter of many shapes.")
        print("these include regular polygons, parallelograms, triangles, etc.. however it can't to calculations with a nonregular polygon after a certain point")
        print()
        print("3D calculator can calculate volume and surface area of many shapes")
        print("these shapes include a prism with many bases, cone, cylinder etc..")
        print("However keep in mind all of the 3D figures are assumed to be regular, except for triangle. (Meaning the bases are regular and equal)")
        print("also keep in mind, the calculations for 3D figures are uniform, meaning there's only 1 formula in place")
        print("most of the times requiring you to have information that can be attainable from the 2D calculator. such as area of the base.")
        print()
        print("please enter return to return to the main menu, from where you can close the system")
    elif choice == 4:
        print("Instructions of the scientific calculator")
        print()
        print("Includes more complex evaluations deviating from the simple calculator")
        print("However it also disallows addition, substraction and other stuff that we would see in an expressive calculator")
        print()
        print("please enter return to return to the main menu, from where you can close the system")

        print("Hope you enjoy, this is the very first project. sorry if there are any bugs present, i tried my best <3")



def calculator_suite():
    while True:
            print()
            print("Welcome to Calculator Suite!")
            print()
            print("Please enter 0 to view instructions.")
            print()
            print("Choose a calculator:")
            print("0 - Instructions")
            print("1 - Simple Calculator")
            print("2 - Unit Converter")
            print("3 - Geometry Calculator")
            print("4 - Scientific Calculator (Not to be confused with expressional calculator)")
            print("stop - Exit")
            choice = input("Choice: ")
            if choice == "1":
                simple_calculator()
            elif choice == "2":
                unit_converter()
            elif choice == "3":
                geometric_calculator()
            elif choice == "4":
                scientific_calculator()
            #elif choice == 0:
                #instructions()
            elif choice == "stop":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")

calculator_suite()





















