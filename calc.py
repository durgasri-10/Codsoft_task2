while True:
    print("\nCalculator")
    print("operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("\nEnter the choice (1to5): ")
    if choice == '5':
        print("Exiting the calculator")
        break
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            result = num1 + num2
            print(f"\n num1 + num2 = result")
        elif choice == '2':
            result = num1 - num2
            print(f"\n num1- num2 = result")
        elif choice == '3':
            result = num1 * num2
            print(f"\n num1 * num2 = result")       
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"\n num1 / num2 = result")
            else:
                print("\nError: Division by zero ")
    else:
        print("\nInvalid choice")