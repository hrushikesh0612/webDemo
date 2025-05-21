def main():
    print("Enter the marks for five subjects:")

    subject_1 = float(input("Subject 1: "))
    subject_2 = float(input("Subject 2: "))
    subject_3 = float(input("Subject 3: "))
    subject_4 = float(input("Subject 4: "))
    subject_5 = float(input("Subject 5: "))

    total_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
    percentage = (total_marks / 500) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 50:
        grade = 'E'
    else:
        grade = 'F'

    print(f"\nTotal Marks: {total_marks} / 500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
