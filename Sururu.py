import datetime+

year = input("Passing Year: ")
name = input("Name of Student: ").upper()
mother = input("Mother's Name: ").upper()
month = input("Month: ").upper()
seat = input("Seat No: ").upper()

subjects = ["MARATHI (01)", "HINDI (02)", "ENGLISH (03)", 
            "MATHEMATICS (71)", "SCIENCE & TECH (72)", "SOCIAL SCIENCE"]

marks = [int(input(f"{sub}: ")) for sub in subjects]

best5_total = sum(sorted(marks, reverse=True)[:5])
percentage = best5_total / 5

failed_count = sum(1 for m in marks if m < 35)
result = "FAILED" if failed_count >= 2 else "PASSED"

if result == "FAILED":
    grade = "F"
elif percentage >= 75:
    grade = "DISTINCTION"
elif percentage >= 60:
    grade = "FIRST CLASS"
elif percentage >= 50:
    grade = "SECOND CLASS"
else:
    grade = "PASS CLASS"

print("\n" + "_"*65)
print("="*65)
print("      MAHARASHTRA STATE BOARD OF SECONDARY EDUCATION")
print(f"                SSC EXAMINATION RESULT {year}")
print("="*65)
print(f"| SEAT NO: {seat:<15} | EXAM MONTH: {month:<10} |")
print(f"| NAME:    {name}")
print(f"| MOTHER:  {mother}")
print("-" * 65)
print("| SUBJECT                   | MAX        | OBTAINED    |")
print("-" * 65)

for sub, mark in zip(subjects, marks):
    print(f"| {sub:<25} | 100        | {mark:<10} |")

print("-" * 65)
print(f"BEST OF 5 TOTAL: {best5_total}/500")
print(f"PERCENTAGE:      {percentage:.2f} %")
print(f"RESULT:          {result}")
print(f"GRADE:           {grade}")
print("-" * 65)
print(f"DATE: {datetime.date.today()}        BOARD SEAL: [MSBSHSE] Mumbai")
print("_" * 65)