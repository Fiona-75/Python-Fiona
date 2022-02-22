name = input("what is your name? ")
start = input("Would you like to use the calculator? Y/N  ").upper()
filename = (name + '.txt')
#print(filename)
FileObject = open(filename, mode = 'a+')
FileObject.write("User: " + name + "\n")
while start == "Y":
    # defining variables

    num1 = float(input("Please insert first number  "))
    choice = str(input("Please enter + - * or /  "))
    num2 = float(input("Please enter second number  "))

    if choice == "+":
        ans = round(num1 + num2,2)
        print("The answer is ", ans)
    elif choice == "-":
        ans = round(num1 - num2,2)
        print("The answer is ", ans)
    elif choice == "*":
        ans = round(num1 * num2,2)
        print("The answer is ", ans)
    elif choice == "/":
        if num2 == 0:
            print("Durrr you cannot divide by zero!!")
        else:
            ans = round(num1 / num2,2)
            print("The answer is ", ans)

    else:
        print("You failed to input + - * or /. What a wally!  ")
    start = input("do you want to continue? Y/N ").upper()
    FileObject.write("Input:")
    FileObject.write(str(num1))
    FileObject.write(str(choice))
    FileObject.write(str(num2))
    FileObject.write("=")
    FileObject.write(str(ans))
    FileObject.write("\n")


else:
    print("Thank you, goodbye!")
    FileObject.close()
