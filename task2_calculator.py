n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
ch=0
while ch<5:
    print()
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit\n")
    ch=int(input("Enter ur choice:"))
    if ch==1:
        n=n1+n2
        print("The result of addition is:",n)
    elif ch==2:
        n=n1-n2
        print("The result of subtraction is:",n)
    elif ch==3:
        n=n1*n2
        print("The result of multiplication is:",n)
    elif ch==4:
        n=n1/n2
        print("The result of division is:",n)
    elif ch==5:
        break
    else:
        print("Invalid choice")
        
