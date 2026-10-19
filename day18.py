# amt=input('enter amount: ')
# percent=input('enter percent: ')
# num=int(input('enter number: '))
# def cal_total(amt,percent,num):
#     total=amt*num*(1+percent)
#     exact_per=total/num
#     return total, exact_per/
# odd  even multiplier
# def odd_even(multiplier):
#     def multiply(num):
#         if num % 2==0:
#             return num * multiplier
#         if num % 5==0:
#             return num * multiplier
#     return (f'{num} is not odd or even')
# def count_vowels_and_consonants(text):
#     vowels = "aeiou"
#     vowel_count = 0
#     consonant_count = 0

#     # Convert the entire string to lowercase so we don't need 'AEIOU'
#     text = text.lower()

#     for char in text:
#         # Step 1: Check if the character is an alphabet letter (ignores 1, 2, !, spaces, etc.)
#         if char.isalpha():
#             # Step 2: Decide if it's a vowel or a consonant
#             if char in vowels:
#                 vowel_count += 1
#             else:
#                 consonant_count += 1

#     return vowel_count, consonant_count


# # --- Example Usage ---
# user_input = input("Enter a word or phrase: ")
# v_count, c_count = count_vowels_and_consonants(user_input)

# print(f"Vowels: {v_count}")
# print(f"Consonants: {c_count}")
# Stu1={'Name':'Savi', 'Average':90}
# Stu2={'Name':'Ravi', 'Average':80}
# Stu3={'Name':'Rani', 'Average':70}
# if Stu1['Average']>79:
#     print(Stu1['Name']+' '+str(Stu1['Average'])+' Grade A')
# else:
#     print(Stu1['Name']+' '+str(Stu1['Average'])+' Grade B')
def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'F'

# Hardcoded student data matching your example
students_data = [
    {"Name": "Rahul", "Avg": 82.33, "Attendance": 80},
    {"Name": "Priya", "Avg": 91.00, "Attendance": 90},
    {"Name": "Amit",  "Avg": 45.67, "Attendance": 60}
]

students = []
passed_count = 0

for s in students_data:
    grade = get_grade(s["Avg"])
    eligibility = "Eligible" if s["Attendance"] >= 75 else "Ineligible"
    
    # Count passed students (Grade A, B, or C)
    if grade in ['A', 'B', 'C']:
        passed_count += 1
        
    students.append({
        "Name": s["Name"],
        "Avg": s["Avg"],
        "Grade": grade,
        "Eligibility": eligibility
    })

# --- PRINTING THE FORMATTED REPORT ---
print("=" * 180)
print("STUDENT PERFORMANCE REPORT")
print("=" * 180)

# enumerate gives us index (0, 1, 2), so i+1 gives 1, 2, 3
for i, student in enumerate(students, start=1):
    # :.2f ensures float values always show 2 decimal places (e.g., 91.00)
    print(f"{i}. Name: {student['Name']:<6} | Avg: {student['Avg']:.2f} | Grade: {student['Grade']} | Exam Eligibility: {student['Eligibility']}")

print("=" * 180)
print(f"Total Students Passed (Grade A, B, or C): {passed_count}/{len(students)}")
print("=" * 180)