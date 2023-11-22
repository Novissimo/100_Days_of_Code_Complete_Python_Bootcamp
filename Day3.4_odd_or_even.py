#Which number do you want to check?

number = int(input("Enter a number to check if its odd or even:"))

#If the number can be divided by 2 with 0 remainder

if number % 2 == 0:
    print("Even")

else:
    print("Odd")