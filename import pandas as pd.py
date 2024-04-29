import pandas as pd

# Load the data from the CSV file into a DataFrame
df = pd.read_csv('C:\\Users\\Ruwaida\\Documents\\Employees.csv')

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Remove decimal places in the Age column
df['Age'] = df['Age'].astype(int)

# 3. Convert USD salary to EGP (Assuming 1 USD = 15 EGP)
df['Salary(EGP)'] = df['Salary(USD)'] * 40
# Print median salary
print("Median salary:", df['Salary(USD)'].median())

# 4. Print some statistics
print("Average age:", df['Age'].mean())
print("Ratio between males and female employees:", df['Gender'].value_counts(normalize=True))

# 5. Write the data to a new CSV file
df.to_csv('new_data.csv', index=False)