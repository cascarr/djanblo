def hi():
    print("Hi there!")
    print("How are you? ")

    while True:
        # accept user input
        usrinp = input("> ")

        # check if user is done
        if usrinp == 'done':
            print("Completed! ")
            break

hi()