# Simple Text Analyzer

text = input("Enter a sentence: ")

print("\n--- Text Analysis ---")
print("Original text:", text)
print("Total characters:", len(text))
print("Total words:", len(text.split()))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Reversed text:", text[::-1])
