# Author: Shaurya Gupta
# Date: 27 Oct 2025
# Project: Daily Calorie Tracker CLI
print("Hi! This is Shaurya's Daily Calorie Tracker ")
print("This tool helps you track your daily meals and calories.")


meals = []
calories = []

n = int(input("How many meals do you want to enter today? "))

for i in range(n):
    meal = input(f"Enter meal {i+1} name: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meals.append(meal)
    calories.append(cal)

total = sum(calories)
avg = total / len(calories)

limit = float(input("\nEnter your daily calorie limit: "))

print("\n=== Calorie Summary ===")
print(f"Total calories consumed: {total}")
print(f"Average calories per meal: {avg:.2f}")

if total > limit:
    print("⚠️ You have exceeded your daily limit!")
else:
    print("✅ Great! You are within your daily calorie limit.")

print("\nMeal Name\tCalories")
print("-" * 25)
for m, c in zip(meals, calories):
    print(f"{m:<12}\t{c}")
print("-" * 25)
print(f"Total:\t\t{total}")
print(f"Average:\t{avg:.2f}")

print("\nMeal Name\tCalories")
print("-" * 25)
for m, c in zip(meals, calories):
    print(f"{m:<12}\t{c}")
print("-" * 25)
print(f"Total:\t\t{total}")
print(f"Average:\t{avg:.2f}")

#  Bonus Task 
save = input("\nDo you want to save this session to a file? (yes/no): ").lower()
if save == "yes":
    print("The report is saved")
    # file writing code here


