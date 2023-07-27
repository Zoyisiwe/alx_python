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
    print_arguments()
'''
import sys

def main():
    # Get the list of arguments passed to the script (excluding the script name itself)
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("Number of arguments:", num_arguments)
    print("List of arguments:", arguments)

if __name__ == "__main__":
    main()
