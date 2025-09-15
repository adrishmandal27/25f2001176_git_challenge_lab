import add
import substract
import multiply
import divide
def main():
    print("Calculator Opened!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("\n------MENU------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            result = add.add_numbers(num1, num2)
            operation_symbol = '+'
        elif choice == '2':
            result = substract.subtract_numbers(num1, num2)
            operation_symbol = '-'
        elif choice == '3':
            result = multiply.multiply_numbers(num1, num2)
            operation_symbol = '*'
        elif choice == '4':
            result = divide.divide_numbers(num1, num2)
            operation_symbol = '/'
        
        print(f"{num1} {operation_symbol} {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4).")

if __name__ == "__main__":
    main()