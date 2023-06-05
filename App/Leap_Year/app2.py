"""
Write a program to check if a year is a leap year
Algorithm
- Get year
- Divide by 4 and check for remainder
- Check if remainder is 0
"""

# Get year
year = input("Enter year to check: ")
# Get remainder
remainder = float(year)%4
if(remainder != 0):
    print(year, "is not leap year ",)
else:
    print(year, "is leap year ",)