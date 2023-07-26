'''Write a program that takes an integer as
input, and creates a mathematical table of
that number.
1 x number = result
2 x number = result
3x number = result
.
.
10 x number = result'''

##############################

def create_math_table(number):
    for i in range(1, 11):
        result = i * number
        print(f"{i} x {number} = {result}")

def main():
    try:
        number = int(input("Enter an integer: "))
        create_math_table(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
