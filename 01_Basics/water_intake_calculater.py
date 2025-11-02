# Water Intake Calculator
# Author: Shivam Vanjara

# Ask user how many glasses of water they drink
glasses = int(input("How many glasses of water do you drink daily? "))

# Define average glass size (in ml)
ml_per_glass = int(input("average glass size in ML : "))

# Calculate total intake
total_ml = glasses * ml_per_glass

# Convert ml → liters
total_liters = total_ml / 1000

print(f"You drink about {total_ml} ml ({total_liters:.2f} liters) of water daily 💧")

# Health check message
if total_liters < 2:
    print("⚠️ You should drink more water!")
elif 2 <= total_liters <= 3.5:
    print("✅ Perfect! You're well hydrated.")
else:
    print("💦 Great job staying hydrated, but don’t overdo it.")
