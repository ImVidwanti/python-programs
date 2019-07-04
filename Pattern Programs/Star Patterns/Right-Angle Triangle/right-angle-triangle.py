user_input = int(input("Enter the number of rows: "))
for length_row in range(1, user_input + 1):
    for length_column in range(1, length_row + 1):
        print("*", end=" ")
    print()
