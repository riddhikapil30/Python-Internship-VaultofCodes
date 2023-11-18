#Task 1: 1)Identify the errors and rectify the code
#Corrected code:
def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def main():
    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()

# Explanation:
#1. Indentation: Corrected the indentation of the `reverse_string` function and the `main` function. Python relies on proper indentation to define blocks of code
#2. Variable Naming: Renamed the variable `reversed` to `reversed_str`. It's not recommended to use the name of a built-in function (`reversed`) for a variable as it may lead to confusion.
#3. Corrected the `if __name__ == "__main__":` block. The underscores in `__name__` and `__main__` were mistakenly written using lowercase letters. They should be uppercase.

