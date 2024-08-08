#codsoft task 2. arithmetic calculator.
print("\n +-*/+-*/+-*/+-*/+-*/ \t ARITHMETIC CALCULATOR \t+-*/+-*/+-*/+-*/+-*/")

def calculator():
    #user input
    #float for decimal number
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation to perform: ")
    print("1. Addition \"+\" ")
    print("2. Subtraction \"-\" ")
    print("3. Multiplication \"*\" ")
    print("4. Division \"/\" ")
    
    choice = input("\n Enter the number to perform arithmetic operation: ")

    #add
    if choice == '1':
        print(num1,'+',num2,'=',num1 + num2)

    #subtract    
    elif choice == '2':
        print(num1,'-',num2,'=',num1 - num2)
    
    #multiply
    elif choice == '3':
        print(num1,'*',num2,'=',num1 * num2)

    #divide    
    elif choice == '4':
        if num2 != 0:
            print(num1,'/',num2,'=',num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")
            return
        
    else:
        print("Invalid choice. Please try again.")
        return
    
#call the function
if __name__ == "__main__":
    calculator()