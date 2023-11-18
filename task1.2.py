#Task 1: 2)

#The input() function returns a string, and comparing it directly with an integer(18) in the if statement, which will result in a TypeError. To fix this, you need to convert the user input (age) to an integer before comparing it.

#Corrected code:
def get_age():
    age_str = input("Please enter your age: ")
    if age_str.isnumeric() and int(age_str) >= 18:
        return int(age_str)
    else:
        return None

def main():
    age = get_age()
    if age is not None:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()
    
#Explanation:
#I made two changes:
#I renamed the variable age to age_str in the get_age function to make it clear that it is a string.
#I used int(age_str) when comparing the age in the if statement to convert it to an integer before the comparison.
#Now the program should work as expected. It checks if the user input is numeric and greater than or equal to 18 before converting it to an integer. If the input is valid, it returns the age; otherwise, it returns None. The main function then prints the appropriate message based on the returned value.