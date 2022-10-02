age = int(input("Enter your age : "))

decades = age // 10
years = age % 10

if(years):
    print(f"You are {decades} decade and {years} year old.")
else:
    print(f"You are {decades} decade old.")


# Enter your age : 29
# You are 2 decade and 9 year old.