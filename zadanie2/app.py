def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result of adding {a} and {b} is {add(a, b)}.")
        print(f"The result of subtracting {b} from {a} is {subtract(a, b)}.")
        print(f"The result of multiplying {a} and {b} is {multiply(a, b)}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
