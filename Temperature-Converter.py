
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Using the formula (Celsius * 9/5) + 32 to convert to Fahrenheit
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # Using the formula (Fahrenheit - 32) * 5/9 to convert to Celsius
    return (fahrenheit - 32) * 5/9

# Main function
def main():
    # Print options to choose from
    print("Temperature Converter")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    
    # Take user input 
    choice = input("Choose an option (1 or 2): ")
    
    # If user chooses Celsius to Fahrenheit conversion
    if choice == "1":
        try:
            # Ask the user to input temperature in Celsius
            celsius = float(input("Enter temperature in Celsius: "))
            # Call the conversion function and display the result
            print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
        except ValueError:
            # Handle invalid input (non-numeric values)
            print("Invalid input! Please enter a valid number.")
    
    # If user chooses Fahrenheit to Celsius conversion
    elif choice == "2":
        try:
            # Ask the user to input temperature in Fahrenheit
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            # Call the conversion function and display the result
            print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
        except ValueError:
            # Handle invalid input (non-numeric values)
            print("Invalid input! Please enter a valid number.")

    # If user enters an invalid option
    else:
        # Notify the user of the invalid choice
        print("Invalid choice! Please enter 1 or 2.")

# Entry point for the program
if __name__ == "__main__":
    # Call the main function 
    main()
