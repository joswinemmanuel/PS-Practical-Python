expenses_count = int(input("Enter the number of expenses this month : "))
print()
expenses = []

for i in range(1, expenses_count+1):
    expenses.append(float(input(f"Enter expense number {i} in $ : ")))

total = sum(expenses)

print("\nYou sent $", total, " this month", sep="")


# Enter the number of expenses this month : 4

# Enter expense number 1 in $ : 132
# Enter expense number 2 in $ : 234.5
# Enter expense number 3 in $ : 32.12
# Enter expense number 4 in $ : 4

# You sent $402.62 this month