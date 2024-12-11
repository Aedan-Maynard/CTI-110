#Aedan Maynard

#11/3/24

#Multiplication table loop

#Using loops to feed back a table and end loop if the input does not fit requirements or the code is told to stop.


def display_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            if user_input < 0:
                print("Negative number cannot be accepted.")
            else:
                display_multiplication_table(user_input)

            # Ask if the user wants to run the program again
            run_again = input("Do you wish to run the program again? yes/no: ").strip().lower()
            if run_again != "yes":
                print("Thank you for using the program. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
