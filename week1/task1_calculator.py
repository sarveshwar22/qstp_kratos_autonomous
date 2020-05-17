num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
op   = int(input(("What operation would you like to perform??\n 1.Addition\n 2.Subtraction\n 3.Multiplication \n 4.Division")))
if op==1:
    print(num1+num2)
elif op==2:
    print(num1-num2)
elif op==3:
    print(num1*num2)
elif op==4:
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("Cannot divide by 0")