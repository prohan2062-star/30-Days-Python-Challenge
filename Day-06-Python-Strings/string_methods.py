# Python String Methods

text = "  learning python is fun  "

print("Original:", text)
print("Stripped:", text.strip())
print("Replace:", text.replace("python", "coding"))
print("Split:", text.split())
print("Starts with learning:", text.strip().startswith("learning"))
print("Ends with fun:", text.strip().endswith("fun"))

message = "Python"

print("Is alphabetic?", message.isalpha())
print("Contains only digits?", message.isdigit())
