def hi(name):
    #
    username = name

    # say hello to user
    print(f"Welcome {username}")

usrinp = input("> Name?? ")

# condition the input
if usrinp == 'done':
    print("Completed! ")
    exit()

elif usrinp.isdigit():
    print("Invalid key")

elif isinstance(usrinp, str):
    #
    hi(usrinp)