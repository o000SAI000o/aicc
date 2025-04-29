from openpyxl import Workbook

print("🔍 Employee Performance Evaluation System")

# Step 1: Input Details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")

print("\nPlease rate the following (scale: 1 - Poor to 10 - Excellent):\n")

# Step 2: Input Scores
punctuality = int(input("Punctuality: "))
communication = int(input("Communication Skills: "))
teamwork = int(input("Teamwork: "))
problem_solving = int(input("Problem Solving: "))
adaptability = int(input("Adaptability: "))
technical_skills = int(input("Technical Skills: "))
leadership = int(input("Leadership: "))
target_achievement = int(input("Target Achievement: "))

# Step 3: Average Score Calculation
total_score = (
    punctuality +
    communication +
    teamwork +
    problem_solving +
    adaptability +
    technical_skills +
    leadership +
    target_achievement
)
average = total_score / 8

# Step 4: Evaluation Logic
if average >= 9:
    grade = "Outstanding"
    feedback = "Exceptional performance across all areas."
elif average >= 7:
    grade = "Very Good"
    feedback = "Consistently good, with strong work ethic."
elif average >= 5:
    grade = "Average"
    feedback = "Meets expectations but has room to improve."
elif average >= 3:
    grade = "Below Average"
    feedback = "Needs to improve in multiple areas."
else:
    grade = "Poor"
    feedback = "Performance is unsatisfactory. Immediate improvement required."

# Step 5: Output to Console
print("\n📋 Final Evaluation Report")
print(f"Name       : {name}")
print(f"Employee ID: {emp_id}")
print(f"Department : {department}")
print(f"Average Score : {average:.2f}")
print(f"Performance Grade : {grade}")
print(f"Manager Feedback  : {feedback}")

# Step 6: Export to Excel
wb = Workbook()
ws = wb.active
ws.title = "Employee Evaluation"

# Headers
ws.append(["Field", "Value"])
ws.append(["Name", name])
ws.append(["Employee ID", emp_id])
ws.append(["Department", department])
ws.append([])

# Scores
ws.append(["Criteria", "Score (out of 10)"])
ws.append(["Punctuality", punctuality])
ws.append(["Communication", communication])
ws.append(["Teamwork", teamwork])
ws.append(["Problem Solving", problem_solving])
ws.append(["Adaptability", adaptability])
ws.append(["Technical Skills", technical_skills])
ws.append(["Leadership", leadership])
ws.append(["Target Achievement", target_achievement])
ws.append([])

# Summary
ws.append(["Average Score", f"{average:.2f}"])
ws.append(["Performance Grade", grade])
ws.append(["Manager Feedback", feedback])

# Save file
excel_filename = f"{emp_id}_Performance_Report.xlsx"
wb.save(excel_filename)

print(f"\n✅ Excel report saved as '{excel_filename}'")
