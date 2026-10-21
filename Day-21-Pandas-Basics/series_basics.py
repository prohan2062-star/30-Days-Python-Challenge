import pandas as pd

numbers = pd.Series([10, 20, 30, 40, 50])

print("Pandas Series:")
print(numbers)

print("\nFirst value:", numbers.iloc[0])
print("Last value:", numbers.iloc[-1])
print("Mean:", numbers.mean())
print("Maximum:", numbers.max())
