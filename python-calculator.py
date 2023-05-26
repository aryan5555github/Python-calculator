while True:
    print('What do you want to do?:')
    print('1: Addition')
    print('2: Subtraction')
    print('3: Multiplication')
    print('4: Division')
    print('Type the number')
    a = input()

    if a == "1":
        print('First number:')
        a = input()
        print('Second number:')
        b = input()
        c = int(a) + int(b)
        print("The sum is:", c)

    elif a == "2":
        print('First number:')
        a = input()
        print('Second number:')
        b = input()
        c = int(a) - int(b)
        print("The difference is:", c)

    elif a == "3":
        print('First number:')
        a = input()
        print('Second number:')
        b = input()
        c = int(a) * int(b)
        print("The product is:", c)

    elif a == "4":
        print('First number:')
        a = input()
        print('Second number:')
        b = input()
        c = int(a) / int(b)
        print("The division result is:", c)

    else:
        print('Invalid operation')
        print("Do you want to continue? (y/n)")
        n = input()
        if n != "y":
            break
        continue

    print("Do you want to continue? (y/n)")
    n = input()
    if n != "y":
        break

print("Press any key to continue...")
input()
