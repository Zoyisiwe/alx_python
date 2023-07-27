'''import sys

def print_arguments():
    arguments = sys.argv[1:] 
    num_arguments = len(arguments)

    print(f"Number of argument(s): {num_arguments}", end="")

    if num_arguments == 0:
        print(".")
    elif num_arguments == 1:
        print(", followed by:")
    else:
        print("s, followed by:")

    for i, arg in enumerate(arguments, start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments()'''

import sys

def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        plural_suffix = "s" if num_arguments > 1 else ""
        print(f"Number of argument(s): {num_arguments}, followed by argument{plural_suffix}:")
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
