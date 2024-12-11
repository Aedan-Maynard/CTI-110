#Aedan Maynard
#10/02/2024
#P3HW2
#Pay Functions

def main ():
    # Get user input
    employee_name = input("Enter the employee's name: ")
    hours_worked = float(input("Enter the number of hours worked this week: "))
    pay_rate = float(input("Enter the employee's pay rate: "))

    # Constants
    OVERTIME_THRESHOLD = 40
    OVERTIME_RATE = 1.5

    # Initialize variables
    regular_hours = hours_worked if hours_worked <= OVERTIME_THRESHOLD else OVERTIME_THRESHOLD
    overtime_hours = max(0, hours_worked - OVERTIME_THRESHOLD)
    
    # Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * OVERTIME_RATE
    gross_pay = regular_pay + overtime_pay

    # Display results
    print("\nEmployee Information:")
    print(f"Employee Name: {employee_name}")
    print(f"Pay Rate: ${pay_rate:.2f}")
    print(f"Hours Worked: {hours_worked:.2f}")
    print(f"Overtime Hours: {overtime_hours:.2f}")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Pay for Regular Hours: ${regular_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")

if __name__ == "__main__":
    main()

