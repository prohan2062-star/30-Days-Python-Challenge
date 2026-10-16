# Parameters, Return Values, and Default Arguments

def introduce(name, course="Python"):
    return f"My name is {name}. I am learning {course}."


def calculate_square(number):
    return number ** 2


print(introduce("Rohan"))
print(introduce("Rohan", "AI and Machine Learning"))

number = int(input("Enter a number: "))
print("Square:", calculate_square(number))
