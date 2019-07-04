user_input = int(input("Enter the number of rows: "))
for length_row in range(0, user_input):
    for spaces in range(0, user_input - length_row - 1):
        print(end=" ")
    for stars in range(0, length_row + 1):
        print("*", end=" ")
    print()
