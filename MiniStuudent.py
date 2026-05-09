import pandas as pd

students = {}

# Add student
def add_student():

    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    students[roll] = {
        "Name": name,
        "Marks": marks
    }

    print("Student Added Successfully!")


# Display students
def display_students():

    if not students:
        print("No records found.")
        return

    print("\nStudent Records:")

    for roll, data in students.items():

        print(roll, data)


# Save to file
def save_to_file():

    try:

        file = open("students.txt", "w")

        for roll, data in students.items():

            file.write(f"{roll},{data['Name']},{data['Marks']}\n")

        file.close()

        print("Records saved successfully!")

    except Exception as e:
        print("Error:", e)


# Generate report using Pandas
def generate_report():

    try:

        df = pd.DataFrame.from_dict(students,
                                    orient='index')

        print("\nStudent Report:")
        print(df)

        print("\nAverage Marks:",
              df["Marks"].mean())

        print("Highest Marks:",
              df["Marks"].max())

    except Exception as e:
        print("Error:", e)


# Main menu
while True:

    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Save Records")
    print("4. Generate Report")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        save_to_file()

    elif choice == 4:
        generate_report()

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")