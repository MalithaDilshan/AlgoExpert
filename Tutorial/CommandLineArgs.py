import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="Give the first number")
    parser.add_argument("--number2", help="Give the second number")
    parser.add_argument("--operation", help="Enter the required operation", choices=["add", "sub", "mul"])

    args = parser.parse_args()

    num1 = int(args.number1)
    num2 = int(args.number2)

    if args.operation == "add":
        print( num1 + num2 )
    elif args.Operation == "sub":
        print( num1 - num2)
    elif args.Operation == "mul":
        print(num1 * num2)
    else:
        print("Operation is not support. Please enter 'add', 'sub' or 'mul' ")
