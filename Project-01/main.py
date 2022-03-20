process = False

while True:
    inp = input("Which process do you want to do? Math or Logic\n").lower().strip()
    if inp == "math":
        process = True  # math
        break
    elif inp == "logic":
        process = False  # logic
        break
    else:
        print("Answer must be math or logic")

# Mathematical Process

if process:
    print('Enter the first number:')
    a = int(input())
    bin_a = format(a, '08b')  # Converting to 8 bit binary
    print("First number is:", a)
    print('It equal', bin_a, 'on binary.')

    print('Enter the second number:')
    b = int(input())
    bin_b = format(b, '08b')  # Converting to 8 bit binary
    print("First number is:", b)
    print('It equal', bin_b, 'on binary.')

    while True:
        math = input('Which mathematical process do you want to do? \n'
                     '+ for addition \n'
                     '- for subtraction \n'
                     '* multiplication \n'
                     '/ for division \n')

        if math == "+":
            result = a + b
            print('Result is:', result)
            print('it equal', format(result, '08b'), 'on binary.')
            break
        elif math == "-":
            result = a - b
            print('Result is:', result)
            print('it equal', format(result, '08b'), 'on binary.')
            break
        elif math == "*":
            result = a * b
            print('Result is:', result)
            print('it equal', format(result, '08b'), 'on binary.')
            break
        elif math == "/":
            result = a / b
            print('Result is:', result)
            print('it equal', format(result, '08b'), 'on binary.')
            break
        else:
            print("Wrong operation, try again")

# Logical Process

if not process:
    print("Numbers MUST be between 0000 and 1111, 0000 and 1111 are included. Numbers also must written in 4 digit.")
    while True:
        print('Enter the first binary number:')
        c = input()
        array_c = [int(i) for i in str(c)]  # Converting to Array
        binary1 = {'0', '1'}
        set_binary1 = set(c)

        if binary1 == set_binary1 or set_binary1 == {'0'} or set_binary1 == {'1'} and len(
                c) == 4:  # Input MUST contain only 1 and 0, and length MUST be 4 bit
            q = input("Inverts all the bits? Yes or No \n").lower().strip()  # NOT logical operator
            while True:
                if q == "yes":
                    if array_c[0] == 1:
                        array_c[0] = 0
                    elif array_c[0] == 0:
                        array_c[0] = 1
                    if array_c[1] == 1:
                        array_c[1] = 0
                    elif array_c[1] == 0:
                        array_c[1] = 1
                    if array_c[2] == 1:
                        array_c[2] = 0
                    elif array_c[2] == 0:
                        array_c[2] = 1
                    if array_c[3] == 1:
                        array_c[3] = 0
                    elif array_c[3] == 0:
                        array_c[3] = 1
                    break
                elif q == "no":
                    break
                else:
                    print("Wrong operation")
            break
        else:
            print("Value is not a binary or not 4 bit binary number.")

    string_c = ''.join([str(elem) for elem in array_c])  # Converting to String
    print(f"First binary number is {string_c}")

    while True:
        print('Enter the second number:')
        d = input()
        array_d = [int(i) for i in str(d)]  # Converting to Array
        int_d = 0
        binary2 = {'0', '1'}
        set_binary2 = set(d)

        if binary2 == set_binary2 or set_binary2 == {'0'} or set_binary2 == {'1'} and len(
                d) == 4:  # Input MUST contain only 1 and 0, and length MUST be 4 bit
            q = input("Inverts all the bits? Yes or No \n").lower().strip()  # NOT logical operator
            while True:
                if q == "yes":
                    if array_d[0] == 1:
                        array_d[0] = 0
                    elif array_d[0] == 0:
                        array_d[0] = 1
                    if array_d[1] == 1:
                        array_d[1] = 0
                    elif array_d[1] == 0:
                        array_d[1] = 1
                    if array_d[2] == 1:
                        array_d[2] = 0
                    elif array_d[2] == 0:
                        array_d[2] = 1
                    if array_d[3] == 1:
                        array_d[3] = 0
                    elif array_d[3] == 0:
                        array_d[3] = 1
                    string_d = ''.join([str(elem) for elem in array_d])  # Converting to String
                    int_d = int(string_d)
                    print(f"New binary number is {string_d}")
                    break
                elif q == "no":
                    break
                else:
                    print("Wrong operation")
            break
        else:
            print("Value is not a binary or not 4 bit binary number.")

    string_d = ''.join([str(elem) for elem in array_d])  # Converting to String
    print(f"Second binary number is {string_d}")

    while True:
        logic = input('Which logical process do you want to do? \n'
                      'AND \n'
                      'OR \n'
                      'XOR \n'
                      'XNOR \n').lower().strip()

        array_logic = [0, 0, 0, 0]

        if logic == "and":

            # First bit
            if array_c[0] == 0 and array_d[0] == 0:
                array_logic[0] = 0
            if array_c[0] == 0 and array_d[0] == 1:
                array_logic[0] = 0
            if array_c[0] == 1 and array_d[0] == 0:
                array_logic[0] = 0
            if array_c[0] == 1 and array_d[0] == 1:
                array_logic[0] = 1

            # Second Bit
            if array_c[1] == 0 and array_d[1] == 0:
                array_logic[1] = 0
            if array_c[1] == 0 and array_d[1] == 1:
                array_logic[1] = 0
            if array_c[1] == 1 and array_d[1] == 0:
                array_logic[1] = 0
            if array_c[1] == 1 and array_d[1] == 1:
                array_logic[1] = 1

            # Third Bit
            if array_c[2] == 0 and array_d[2] == 0:
                array_logic[2] = 0
            if array_c[2] == 0 and array_d[2] == 1:
                array_logic[2] = 0
            if array_c[2] == 1 and array_d[2] == 0:
                array_logic[2] = 0
            if array_c[2] == 1 and array_d[2] == 1:
                array_logic[2] = 1

            # Fourth Bit
            if array_c[3] == 0 and array_d[3] == 0:
                array_logic[3] = 0
            if array_c[3] == 0 and array_d[3] == 1:
                array_logic[3] = 0
            if array_c[3] == 1 and array_d[3] == 0:
                array_logic[3] = 0
            if array_c[3] == 1 and array_d[3] == 1:
                array_logic[3] = 1

            string_logic = ''.join([str(elem) for elem in array_logic])  # Converting to String
            print(f"Result of the AND operation: {string_logic}")

            break

        elif logic == "or":

            # First bit
            if array_c[0] == 0 and array_d[0] == 0:
                array_logic[0] = 0
            if array_c[0] == 0 and array_d[0] == 1:
                array_logic[0] = 1
            if array_c[0] == 1 and array_d[0] == 0:
                array_logic[0] = 1
            if array_c[0] == 1 and array_d[0] == 1:
                array_logic[0] = 1

            # Second Bit
            if array_c[1] == 0 and array_d[1] == 0:
                array_logic[1] = 0
            if array_c[1] == 0 and array_d[1] == 1:
                array_logic[1] = 1
            if array_c[1] == 1 and array_d[1] == 0:
                array_logic[1] = 1
            if array_c[1] == 1 and array_d[1] == 1:
                array_logic[1] = 1

            # Third Bit
            if array_c[2] == 0 and array_d[2] == 0:
                array_logic[2] = 0
            if array_c[2] == 0 and array_d[2] == 1:
                array_logic[2] = 1
            if array_c[2] == 1 and array_d[2] == 0:
                array_logic[2] = 1
            if array_c[2] == 1 and array_d[2] == 1:
                array_logic[2] = 1

            # Fourth Bit
            if array_c[3] == 0 and array_d[3] == 0:
                array_logic[3] = 0
            if array_c[3] == 0 and array_d[3] == 1:
                array_logic[3] = 1
            if array_c[3] == 1 and array_d[3] == 0:
                array_logic[3] = 1
            if array_c[3] == 1 and array_d[3] == 1:
                array_logic[3] = 1

            string_logic = ''.join([str(elem) for elem in array_logic])  # Converting to String
            print(f"Result of the OR operation: {string_logic}")

            break

        elif logic == "xor":

            # First bit
            if array_c[0] == 0 and array_d[0] == 0:
                array_logic[0] = 0
            if array_c[0] == 0 and array_d[0] == 1:
                array_logic[0] = 1
            if array_c[0] == 1 and array_d[0] == 0:
                array_logic[0] = 1
            if array_c[0] == 1 and array_d[0] == 1:
                array_logic[0] = 0

            # Second Bit
            if array_c[1] == 0 and array_d[1] == 0:
                array_logic[1] = 0
            if array_c[1] == 0 and array_d[1] == 1:
                array_logic[1] = 1
            if array_c[1] == 1 and array_d[1] == 0:
                array_logic[1] = 1
            if array_c[1] == 1 and array_d[1] == 1:
                array_logic[1] = 0

            # Third Bit
            if array_c[2] == 0 and array_d[2] == 0:
                array_logic[2] = 0
            if array_c[2] == 0 and array_d[2] == 1:
                array_logic[2] = 1
            if array_c[2] == 1 and array_d[2] == 0:
                array_logic[2] = 1
            if array_c[2] == 1 and array_d[2] == 1:
                array_logic[2] = 0

            # Fourth Bit
            if array_c[3] == 0 and array_d[3] == 0:
                array_logic[3] = 0
            if array_c[3] == 0 and array_d[3] == 1:
                array_logic[3] = 1
            if array_c[3] == 1 and array_d[3] == 0:
                array_logic[3] = 1
            if array_c[3] == 1 and array_d[3] == 1:
                array_logic[3] = 0

            string_logic = ''.join([str(elem) for elem in array_logic])  # Converting to String
            print(f"Result of the XOR operation: {string_logic}")

            break

        elif logic == "xnor":

            # First bit
            if array_c[0] == 0 and array_d[0] == 0:
                array_logic[0] = 1
            if array_c[0] == 0 and array_d[0] == 1:
                array_logic[0] = 0
            if array_c[0] == 1 and array_d[0] == 0:
                array_logic[0] = 0
            if array_c[0] == 1 and array_d[0] == 1:
                array_logic[0] = 1

            # Second Bit
            if array_c[1] == 0 and array_d[1] == 0:
                array_logic[1] = 1
            if array_c[1] == 0 and array_d[1] == 1:
                array_logic[1] = 0
            if array_c[1] == 1 and array_d[1] == 0:
                array_logic[1] = 0
            if array_c[1] == 1 and array_d[1] == 1:
                array_logic[1] = 1

            # Third Bit
            if array_c[2] == 0 and array_d[2] == 0:
                array_logic[2] = 1
            if array_c[2] == 0 and array_d[2] == 1:
                array_logic[2] = 0
            if array_c[2] == 1 and array_d[2] == 0:
                array_logic[2] = 0
            if array_c[2] == 1 and array_d[2] == 1:
                array_logic[2] = 1

            # Fourth Bit
            if array_c[3] == 0 and array_d[3] == 0:
                array_logic[3] = 1
            if array_c[3] == 0 and array_d[3] == 1:
                array_logic[3] = 0
            if array_c[3] == 1 and array_d[3] == 0:
                array_logic[3] = 0
            if array_c[3] == 1 and array_d[3] == 1:
                array_logic[3] = 1

            string_logic = ''.join([str(elem) for elem in array_logic])  # Converting to String
            print(f"Result of the XNOR operation: {string_logic}")

            break

        else:
            print("Wrong operation, try again")
