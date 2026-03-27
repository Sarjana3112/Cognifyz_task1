import random

def half_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def inverted_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def full_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def inverted_full_pyramid(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def floyd_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

def square_pattern(rows):
    for i in range(rows):
        for j in range(1, rows + 1):
            print(j, end=" ")
        print()

def reverse_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def right_aligned_triangle(rows):
    for i in range(1, rows + 1):
        print("  " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def diamond_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def continuous_number_pyramid(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()


# Main Program (Pattern Selector)
while True:
    print("\n NUMBER PATTERN GENERATOR")
    print("1. Half Pyramid")
    print("2. Inverted Half Pyramid")
    print("3. Full Pyramid")
    print("4. Inverted Full Pyramid")
    print("5. Floyd’s Triangle")
    print("6. Square Pattern")
    print("7. Reverse Number Pattern")
    print("8. Right-Aligned Triangle")
    print("9. Diamond Pattern")
    print("10. Continuous Number Pyramid")
    print("11. Exit")

    choice = int(input("Enter your choice (1-11): "))
    
    if choice == 11:
        print("Exiting Program...")
        break

    rows = int(input("Enter number of rows: "))
    print("\nGenerated Pattern:\n")

    if choice == 1:
        half_pyramid(rows)
    elif choice == 2:
        inverted_half_pyramid(rows)
    elif choice == 3:
        full_pyramid(rows)
    elif choice == 4:
        inverted_full_pyramid(rows)
    elif choice == 5:
        floyd_triangle(rows)
    elif choice == 6:
        square_pattern(rows)
    elif choice == 7:
        reverse_number_pattern(rows)
    elif choice == 8:
        right_aligned_triangle(rows)
    elif choice == 9:
        diamond_pattern(rows)
    elif choice == 10:
        continuous_number_pyramid(rows)
    else:
        print("Invalid choice! Please select between 1 and 11.")